#include "shell.h"

void our_print(const char *print)
{
	write(STDOUT_FILENO, print, strlen(print));
}
