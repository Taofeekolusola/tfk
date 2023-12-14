#include "our_shell.h"

void our_print(const char *string)
{
	write(STDOUT_FILENO, string, strlen(string));
}
