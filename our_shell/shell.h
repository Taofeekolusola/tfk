#ifndef OUR_SHELL_H
#define OUR_SHELL_H
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdbool.h>
ssize_t promptprint(const char* prompt);
ssize_t _print(const char* message);
void execmd(char **av);
char *get_location(char *command);
//ssize_t our_print(const char* message);
#endif
