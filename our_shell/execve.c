#include "shell.h"
void execmd(char **av){
    char *command = NULL;
    char *actual_command = NULL;
    if (av){
/* get the command */
        command = av[0];
/* generate the path to this command before passing it to execve */
        actual_command = get_location(command);
/* execute the command with execve */
        if (execve(actual_command, av, NULL) == -1)
        {
            perror("Error:");
        }
    }
}
