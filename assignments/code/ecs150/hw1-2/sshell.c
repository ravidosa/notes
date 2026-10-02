#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define CMDLINE_MAX 512
#define ARGS_MAX 16
#define PIPE_MAX 3

pid_t bg_pids[PIPE_MAX + 1];
int bg_cmd_ct = 0;
char bg_cmd[CMDLINE_MAX];

int parse(char *cmd, char *args[])
{
    int i = 0;
    if (cmd[0] == '\0' || cmd[0] == '\n') {
        fprintf(stderr, "Error: missinger command\n");
        return -1;
    }

    char *arg = strtok(cmd, " ");

    while (arg != NULL && i < ARGS_MAX) {
        args[i] = arg;
        i++;
        arg = strtok(NULL, " ");
    }

    if (arg != NULL) {
        fprintf(stderr, "Error: too many process arguments\n");
        return -1;
    }
    if (i == 0) {
        fprintf(stderr, "Error: missing command\n");
        return -1;
    }

    args[i] = NULL;
    return i;
}

int redirect(char *cmd, char **file, int *append)
{
    char *redir = strchr(cmd, '>');

    if (redir) {
        *redir = '\0';
        redir++;
        if (*redir == '>') {
            *append = 1;
            redir++;
        }

        /* strip leading and trailing whitespace from file */
        while (*redir == ' ') {
            redir++;
        }
        *file = redir;
        char *end = *file + strlen(*file) - 1;
        while (end > *file && *end == ' ') {
            *end = '\0';
            end--;
        }
        if (strlen(*file) == 0) {
            fprintf(stderr, "Error: no output file\n");
            return -1;
        }
        if (strchr(*file, '|')) {
            fprintf(stderr, "Error: mislocated output redirection\n");
            return -1;
        }
    }
    return 0;
}

int execute(char *args[], char *file, int append)
{
    if (file) {
        int flags = append ? (O_WRONLY | O_CREAT | O_APPEND)
                           : (O_WRONLY | O_CREAT | O_TRUNC);
        int fd = open(file, flags, 0644);
        if (fd < 0) {
            fprintf(stderr, "Error: cannot open output file\n");
            return -1;
        }
        dup2(fd, STDOUT_FILENO);
        close(fd);
    }
    execvp(args[0], args);
    fprintf(stderr, "Error: command not found\n");
    return -1;
}

void check_bg_job(int sig)
{
    (void)sig;
    if (bg_cmd_ct > 0) {
        int bg_done = 1;
        int exit_status[bg_cmd_ct];

        for (int i = 0; i < bg_cmd_ct; i++) {
            int status;
            pid_t res = waitpid(bg_pids[i], &status, WNOHANG);
            if (res > 0) {
                exit_status[i] = WEXITSTATUS(status);
            } else {
                bg_done = 0;
                break;
            }
        }

        if (bg_done) {
            fprintf(stderr, "+ completed '%s' ", bg_cmd);
            for (int i = 0; i < bg_cmd_ct; i++) {
                fprintf(stderr, "[%d]", exit_status[i]);
            }
            fprintf(stderr, "\n");

            bg_cmd_ct = 0;
            bg_cmd[0] = '\0';
        }
    }
}

int main(void)
{
    char cmd[CMDLINE_MAX];
    char *eof;

    signal(SIGCHLD, check_bg_job);

    while (1) {
        char *nl_ptr;

        /* Print prompt */
        printf("sshell@ucd$ ");
        fflush(stdout);

        /* Get command line */
        eof = fgets(cmd, CMDLINE_MAX, stdin);
        if (!eof) {
            /* Make EOF equate to exit */
            strncpy(cmd, "exit\n", CMDLINE_MAX);
        }

        /* Print command line if stdin is not provided by terminal */
        if (!isatty(STDIN_FILENO)) {
            printf("%s", cmd);
            fflush(stdout);
        }

        /* Remove trailing newline from command line */
        nl_ptr = strchr(cmd, '\n');
        if (nl_ptr) {
            *nl_ptr = '\0';
        }

        int valid_bg = 0;
        char *bg = strrchr(cmd, '&');
        char cmd_bg_tmp[CMDLINE_MAX];

        if (bg) {
            strncpy(cmd_bg_tmp, cmd, CMDLINE_MAX);

            char *chk = bg + 1;
            while (*chk == ' ') {
                chk++;
            }
            if (*chk == '\0') {
                valid_bg = 1;
                *bg = '\0';
            }
            if (!valid_bg) {
                fprintf(stderr, "Error: mislocated background sign\n");
            }
        }

        /* Builtin commands */
        if (!strcmp(cmd, "exit")) {
            if (bg_cmd_ct > 0) {
                fprintf(stderr, "Error: active job still running\n");
                fprintf(stderr, "+ completed 'exit' [1]\n");
            } else {
                fprintf(stderr, "Bye...\n");
                fprintf(stderr, "+ completed 'exit' [0]\n");
                break;
            }
        }

        else if (!strcmp(cmd, "pwd")) {
            char cwd[CMDLINE_MAX];
            if (getcwd(cwd, CMDLINE_MAX) == NULL) {
                perror("pwd");
                exit(1);
            }
            printf("%s\n", cwd);
            fprintf(stderr, "+ completed 'pwd' [0]\n");
        }

        else if (!strncmp(cmd, "cd ", 3)) {
            char *dir = cmd + 3;
            while (*dir == ' ') {
                dir++;
            }
            if (chdir(dir) == -1) {
                fprintf(stderr, "Error: cannot cd into directory\n");
            }
            fprintf(stderr, "+ completed '%s' [0]\n", cmd);
        }

        else {
            /* count pipes */
            int pipe_ct = 0;
            for (char *p = cmd; *p; p++) {
                if (*p == '|') {
                    pipe_ct++;
                }
                if (pipe_ct == PIPE_MAX) {
                    break;
                }
            }

            /* tokenize using | */
            int cmd_ct = pipe_ct + 1;
            char cmd_tmp[CMDLINE_MAX];
            strncpy(cmd_tmp, cmd, CMDLINE_MAX);

            char *cmds[cmd_ct];
            int i = 0;
            char *cmd_pipe = strtok(cmd, "|");

            while (cmd_pipe != NULL && i < cmd_ct) {
                cmds[i] = cmd_pipe;
                i++;
                cmd_pipe = strtok(NULL, "|");
            }

            if (cmd_ct > i) {
                fprintf(stderr, "Error: missing command\n");
                continue;
            } else if (cmd_ct < i) {
                fprintf(stderr, "AlanError\n");
                continue;
            }

            int pipes[pipe_ct][2];
            for (int i = 0; i < pipe_ct; i++) {
                if (pipe(pipes[i]) == -1) {
                    perror("pipe");
                    exit(1);
                }
            }

            pid_t pids[cmd_ct];
            for (int i = 0; i < cmd_ct; i++) {
                pids[i] = fork();
                if (pids[i] == 0) {
                    /* connect stdin */
                    if (i > 0) {
                        dup2(pipes[i - 1][0], STDIN_FILENO);
                    }
                    /* connect stdout */
                    if (i < cmd_ct - 1) {
                        dup2(pipes[i][1], STDOUT_FILENO);
                    }
                    for (int j = 0; j < pipe_ct; j++) {
                        close(pipes[j][0]);
                        close(pipes[j][1]);
                    }

                    char *file = NULL;
                    int append = 0;
                    if (i == cmd_ct - 1) {
                        if (redirect(cmds[i], &file, &append) == -1) {
                            exit(1);
                        }
                    } else {
                        if (strchr(cmds[i], '>')) {
                            fprintf(stderr,
                                    "Error: mislocated output redirection\n");
                            exit(1);
                        }
                    }

                    char *args[ARGS_MAX + 1];
                    if (parse(cmds[i], args) == -1) {
                        exit(1);
                    }
                    if (execute(args, file, append) == -1) {
                        exit(1);
                    }
                } else if (pids[i] < 0) {
                    perror("fork");
                    exit(1);
                }
            }

            for (int i = 0; i < pipe_ct; i++) {
                close(pipes[i][0]);
                close(pipes[i][1]);
            }

            if (valid_bg) {
                for (int i = 0; i < cmd_ct; i++) {
                    bg_pids[i] = pids[i];
                }
                bg_cmd_ct = cmd_ct;
                strncpy(bg_cmd, cmd_bg_tmp, CMDLINE_MAX);
            } else {

                int exit_status[cmd_ct];
                for (int i = 0; i < cmd_ct; i++) {
                    int status;
                    waitpid(pids[i], &status, 0);
                    exit_status[i] = WEXITSTATUS(status);
                }
                fprintf(stderr, "+ completed '%s' ", cmd_tmp);
                for (int i = 0; i < cmd_ct; i++) {
                    fprintf(stderr, "[%d]", exit_status[i]);
                }
                fprintf(stderr, "\n");
            }
        }
    }

    return EXIT_SUCCESS;
}
