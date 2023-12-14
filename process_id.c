#include <stdio.h>
#include <unistd.h>

int main()
{
	int num = 17;
	
	pid_t process_id;

	process_id = getppid();

	printf("%d\n", num);
	printf("the parent process_id is %u\n", process_id);
}
