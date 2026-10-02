#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define CMDLINE_MAX 512

int main(void)
{
    char cmd[CMDLINE_MAX];
    char *eof;

    while (1) {
        char *nl_ptr;
        int retval;
        pid_t pid;

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

        /* Builtin command */
        if (!strcmp(cmd, "exit")) {
            fprintf(stderr, "Bye...\n");
            fprintf(stderr, "+ completed 'exit' [0]\n");
            break;
        }

        else {
            /* Regular command */
            pid = fork();
            if (pid == 0) {
                /* child */
                char *args[16];

                int i = 0;
                char *token = strtok(cmd, " ");
                while (token != NULL && i < 16) {
                    args[i] = token;
                    i++;
                    token = strtok(NULL, " ");
                }

                if (token != NULL) {
                    fprintf(stderr, "Error: too many process arguments\n");
                    exit(1);
                }
                args[i] = NULL;
                execvp(cmd, args);
                fprintf(stderr, "Error: command not found\n");
                exit(1);
            }

            else if (pid > 0) {
                /* parent */
                int status;
                waitpid(pid, &status, 0);
                retval = WEXITSTATUS(status);
                if (retval == 0) {
                    fprintf(stderr, "+ completed '%s' [%d]\n", cmd, retval);
                }
            }

            else {
                perror("fork");
                exit(1);
            }
        }
    }

    return EXIT_SUCCESS;
}
