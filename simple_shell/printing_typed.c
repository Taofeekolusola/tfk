#include "our_shell.h"

int main(int ac, char **argv){
  char *prompt = "(Eshell) $ ";
  char *lineptr;
  size_t n = 0; 

  printf("%s", prompt);
  getline(&lineptr, &n, stdin);
  printf("%s\n", lineptr);

  free(lineptr);
  return (0);
}
