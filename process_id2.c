#include <stdio.h>
#include <unistd.h>

int main()
{
	int num = 20;

	pid_t i_d;

	i_d = getpid();

	printf("%d\n", num);
	printf("%u\n", i_d);
}
