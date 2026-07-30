#!/bin/bash

# Safer execution
# -e: exit immediately if a command fails
# -E: Safer -e option for traps
# -u: fail if a variable is used unset
# -o pipefail: exit immediately if command in a pipe fails
#set -eEuo pipefail
# -x: print each command before executing (great for debugging)
#set -x

# Convenient values
SCRIPT_NAME=$(basename "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

# Default program values
SSHELL_EXEC="${SCRIPT_DIR}/sshell"
TEST_CASE="all"

#
# Logging helpers
#
log() {
    echo -e "${*}"
}
info() {
    log "Info: ${*}"
}
warning() {
    log "Warning: ${*}"
}
error() {
    log "Error: ${*}"
}
die() {
    error "${*}"
    exit 1
}

#
# Line comparison
#
select_line() {
    # 1: string
    # 2: line to select
    echo "${1}" | sed "${2}q;d"
}

fail() {
    # 1: got
    # 2: expected
    log "Fail: got '${1}' but expected '${2}'"
}

pass() {
    # got
    log "Pass: ${1}"
}

compare_lines() {
    # 1: output
    # 2: expected
    # 3: score (output)
    declare -a output_lines=("${!1}")
    declare -a expect_lines=("${!2}")
    local -n __score=$3
    local partial="0"

    # Amount of partial credit for each correct output line
    local step
    step=$(python3 -c "print(1.0 / ${#expect_lines[@]})")

    # Compare lines, two by two
    for i in ${!output_lines[*]}; do
        if [[ "${output_lines[${i}]}" == "${expect_lines[${i}]}" ]]; then
            pass "${output_lines[${i}]}"
            partial=$(python3 -c "print(${partial} + ${step})")
        else
            fail "${output_lines[${i}]}" "${expect_lines[${i}]}"
        fi
    done

    # Return final score
    __score="${partial}"
}

#
# Run generic test case
#
run_test_case () {
    # 1: multi-line string to feed to the shell
    # 2: (optional) tool cmd
    #    (e.g., "strace", "valgrind --leak-check=full --error-exitcode=1")
    local cmdline="${1}"
    local tool_cmd="${2:-}"

    # Check sshell path
    [[ -x ${SSHELL_EXEC} ]] || \
        die "Cannot find executable '${SSHELL_EXEC}'"

    # These are global variables after the test has run so clear them out now
    unset STDOUT STDERR RET

    # Create temp files for getting stdout and stderr
    local outfile errfile
    outfile=$(mktemp)
    errfile=$(mktemp)

    # Execution command
    local exec_cmd
    if [[ -n "${tool_cmd}" ]]; then
        IFS=" " read -r -a exec_cmd <<< "${tool_cmd}"
    fi
    exec_cmd+=("${SSHELL_EXEC}")

    bash -c "echo -e \"${cmdline}\" | ${exec_cmd[*]}" >"${outfile}" 2>"${errfile}"

    # Get the return status, stdout and stderr of the test case
    RET="${?}"
    STDOUT=$(<"${outfile}")
    STDERR=$(<"${errfile}")

    # Clean up temp files
    rm -f "${outfile}"
    rm -f "${errfile}"
}

#
# Test cases
#
TEST_CASES=()

## Cannot use system()
system_syscall() {
    info "Ensure fork+exec is used instead of system"

    run_test_case "ls\nexit\n" "strace"

    local line_array=("$(echo "${STDERR}" | grep "clone3")")
    local corr_array=("")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("system_syscall")

## Exit needs to exist no matter what!
builtin_exit() {
    info "Check that we can exit from your sshell"

    run_test_case "exit\n"

    local line_array=()
    line_array+=("$(select_line "${STDERR}" "1")")
    line_array+=("$(select_line "${STDERR}" "2")")
    local corr_array=()
    corr_array+=("Bye...")
    corr_array+=("+ completed 'exit' [0]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("builtin_exit")

exit_retval() {
    info "Check the completion message from exit"

    run_test_case "exit\n"

    local line_array=("${RET}")
    local corr_array=("0")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("exit_retval")

## Commands with no arguments
cmd_no_arg_1() {
    info "Test a command with no argument (ls) and exit"

    touch titi toto
    run_test_case "ls\nexit\n"
    rm titi toto

    local line_array=()
    line_array+=("$(select_line "${STDOUT}" "2")")
    line_array+=("$(select_line "${STDOUT}" "3")")
    local corr_array=()
    corr_array+=("titi")
    corr_array+=("toto")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_no_arg_1")

cmd_no_arg_2() {
    info "Test another command with no argument (echo) and exit"

    run_test_case "echo\nexit\n"

    local line_array=("$(select_line "${STDOUT}" "2")")
    local corr_array=("")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_no_arg_2")

## Command without argument -- error
cmd_not_found() {
    info "Test an non-existing command"

    run_test_case "commandthatdoesntexists\nexit\n"

    local line_array=()
    line_array+=("$(select_line "${STDERR}" "1")")
    line_array+=("$(select_line "${STDERR}" "2")")
    local corr_array=()
    corr_array+=("Error: command not found")
    corr_array+=("+ completed 'commandthatdoesntexists' [1]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_not_found")

## Commands with arguments
cmd_one_arg() {
    info "Test a command with one argument (ls) and exit"

    mkdir dir_test && touch dir_test/lstest
    run_test_case "ls dir_test\nexit\n"
    rm -rf dir_test

    local line_array=("$(select_line "${STDOUT}" "2")")
    local corr_array=("lstest")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_one_arg")

cmd_one_arg_success() {
    info "Same as above with valid argument but check completion message"

    mkdir dir_test && touch dir_test/lstest
    run_test_case "ls dir_test\nexit\n"
    rm -rf dir_test

    local line_array=("$(select_line "${STDERR}" "1")")
    local corr_array=("+ completed 'ls dir_test' [0]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_one_arg_success")

cmd_one_arg_fail() {
    info "Same as above with invalid argument"

    rm -rf dir_test
    run_test_case "ls dir_test\nexit\n"

    local line_array=("$(select_line "${STDERR}" "2")")
    local corr_array=("+ completed 'ls dir_test' [2]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_one_arg_fail")

cmd_16_args() {
    info "Test command with 16 arguments total"

    run_test_case "echo a a a a a a a a a a a a a a a\nexit\n"

    local line_array=("$(select_line "${STDOUT}" "2")")
    local corr_array=("a a a a a a a a a a a a a a a")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_16_args")

cmd_one_arg_whitespace() {
    info "Test command with one argument that contains many spaces (before the execute name and between the executable and the argument)"

    mkdir dir_test && touch dir_test/lstest
    run_test_case "    ls    dir_test\nexit\n"
    rm -rf dir_test

    local line_array=()
    line_array+=("$(select_line "${STDOUT}" "2")")
    line_array+=("$(select_line "${STDERR}" "1")")
    local corr_array=()
    corr_array+=("lstest")
    corr_array+=("+ completed '    ls    dir_test' [0]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cmd_one_arg_whitespace")

## Builtin commands
cd_pwd() {
    info "Test cd and pwd"

    run_test_case "mkdir -p dir_test\ncd dir_test\npwd\nexit\n"
    rm -rf dir_test

    local line_array=()
    line_array+=("$(select_line "${STDOUT}" "4")")
    line_array+=("$(select_line "${STDERR}" "2")")
    local corr_array=()
    corr_array+=("$PWD/dir_test")
    corr_array+=("+ completed 'cd dir_test' [0]")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("cd_pwd")

## Output redirection
out_redir() {
    info "Simple output redirection"

    run_test_case "echo hello > t\ncat t\nexit\n"
    rm -f t

    local line_array=("$(select_line "${STDOUT}" "3")")
    local corr_array=("hello")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("out_redir")

## Piped commands
pipe() {
    info "Simple job with one pipe"

    echo -e "HELLO world\nhello WORLD" > t
    run_test_case "cat t | grep hello\nexit\n"
    rm -f t

    local line_array=("$(select_line "${STDOUT}" "2")")
    local corr_array=("hello WORLD")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("pipe")

## Extra feature #1: stdout appending
stdout_app_simple() {
    info "Simple appending output redirection"

    run_test_case "echo toto > t\necho titi >> t\ncat t\nexit\n"
    rm -f t

    local line_array=()
    line_array+=("$(select_line "${STDOUT}" "4")")
    line_array+=("$(select_line "${STDOUT}" "5")")
    local corr_array=()
    corr_array+=("toto")
    corr_array+=("titi")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("stdout_app_simple")

## Extra feature #2: background command
background() {
    info "One simple command in background"

    info "(Note: this test might hang a little)"
    run_test_case "sleep 1&\nsleep 2\nexit\n"

    local line_array=()
    line_array+=("$(select_line "${STDOUT}" "2")")
    line_array+=("$(select_line "${STDERR}" "1")")
    line_array+=("$(select_line "${STDERR}" "2")")
    line_array+=("$(select_line "${STDERR}" "3")")
    local corr_array=()
    corr_array+=("sshell@ucd$ sleep 2")
    corr_array+=("+ completed 'sleep 1&' [0]")
    corr_array+=("+ completed 'sleep 2' [0]")
    corr_array+=("Bye...")

    local score
    compare_lines line_array[@] corr_array[@] score
    log "${score}"
}
TEST_CASES+=("background")

#
# Main functions
#
parse_argvs() {
    local OPTIND opt

    while getopts "h?s:t:" opt; do
        case "$opt" in
        h|\?)
            echo "${SCRIPT_NAME}: [-s <sshell_path>] [-t <test_case>]" 1>&2
            exit 0
            ;;
        s)  SSHELL_EXEC=$(readlink -f -- "${OPTARG}")
            ;;
        t)  TEST_CASE="${OPTARG}"
            ;;
        esac
    done
}

check_vals() {
    # Check sshell path
    [[ -x ${SSHELL_EXEC} ]] || \
        die "Cannot find executable '${SSHELL_EXEC}'"

    # Check test case
    [[ " ${TEST_CASES[*]} all " =~ ${TEST_CASE} ]] || \
        die "Cannot find test case '${TEST_CASE}'"
}

grade() {
    # Make testing directory
    local tmpdir
    tmpdir=$(mktemp -d --tmpdir=.)
    cd "${tmpdir}" || die "Cannot cd into temp directory"

    # Run test case(s)
    if [[ "${TEST_CASE}" == "all" ]]; then
        # Run all test cases
        for t in "${TEST_CASES[@]}"; do
            log "--- Running test case: ${t} ---"
            ${t}
            log "\n"
        done
    else
        # Run specific test case
        ${TEST_CASE}
    fi

    # Cleanup testing directory
    cd ..
    rm -rf "${tmpdir}"
}

parse_argvs "$@"
check_vals
grade
