#include "our_shell.h"

void our_exec_command(const char *order)
{
	pid_t child_pid = for();

	if (child_pid == -1)
	{
		perror("fork");
		exit(EXIT_FAILURE);
	}
	else if (chikd_pid == 0)
	{
		execvp(order, order, (char *) NULL);
		perrer("execvp");
		exit(EXIT_FAILURE);
	}
	else
	{
		wait(NULL);
	}
}
