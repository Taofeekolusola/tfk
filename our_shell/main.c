#include "shell.h"
int main(int ac, char** av)
{
    char* prompt = "TAshell $ ";
    size_t n = 0;
    char* full_command = NULL;
    char *copy_command = NULL;
    const char *delim = " \n";
    int num_tokens = 0;
    char *token;
    int i;
    int counter;
    ssize_t no_of_char_read;
/* declaring void variables */
    (void)ac;
/* Create a loop for the shell's prompt */
    while(1)
    {
    promptprint(prompt);
    no_of_char_read = getline(&full_command, &n, stdin);
/* check if the getline function failed or reached EOF or user use CTRL + D */
        if(no_of_char_read == -1)
        {
        //our_print("Exiting the shell...\n");
        perror("Error reading input");
        return (-1);
        }
/* allocate space for a copy of the lineptr */
   copy_command = malloc(sizeof(char) * no_of_char_read);
        if (copy_command == NULL)
        {
            perror("tsh: memory allocation error");
            return (-1);
        }
/* copy lineptr to lineptr_copy */
    strcpy(copy_command, full_command);
/*split the string (full_command) into an array of words*/
/* calculate the total number of tokens */
    token = strtok(full_command, delim);
    while (token != NULL)
    {
        num_tokens++;
        token = strtok(NULL, delim);
    }
     num_tokens++;
/* Allocate space to hold the array of strings */
    av = malloc(sizeof(char *) * num_tokens);
/* Store each token in the argv array */
    token = strtok(copy_command, delim);
    for (i = 0; token != NULL; i++)
    {
        av[i] = malloc(sizeof(char) * strlen(token) + 1);
        strcpy(av[i], token);
        token = strtok(NULL, delim);
    }
      //  av[i] = NULL;
/* print the content of argv*/
        for (counter = 0; counter <num_tokens-1; counter++){
            _print(av[counter]);
        }
        for (counter = 0; counter < num_tokens - 1; counter++) {
            free(av[counter]);
        }
   //our_print(full_command);
/* free up allocated memory */
    //free(av[counter]);
    //av[counter] = NULL;
    free(av);
   // av = NULL;
    //copy_command = NULL;
    }
    free(full_command);
   full_command = NULL;
    free(copy_command);
    return (0);
}
