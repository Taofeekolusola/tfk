#include <stdio.h>
#include <unistd.h>

int main(void)
{
	pid_t pid;

	pid_t ppid;

	pid = fork();

	if (pid == -1)
	{
		perror("unsuccessful");
		return 1;
	}
	
	if (fork == 0)
	{
		sleep(5);
		printf("i am the child\n");
	}
	else
		printf("parent id = %u\n", ppid);
		ppid = getppid();
	return 0;
}
