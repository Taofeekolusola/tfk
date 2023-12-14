#include "shell.h"

int main(int ac, char **argv)
{
  char *display = "T.Shell=$ ";
  char *lineptr;
  size_t n = 0; 

  /* declaring void variables */
  (void)ac; (void)argv;

  our_print(display);
  getline(&lineptr, &n, stdin);
  our_print(lineptr);

  free(lineptr);
  return (0);
}
