#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int count, sum;

	if (argc > 1)
	{
		for (count = 1; count < argc; count++)
		{	
			printf("argv[%d] = %s\n", count, argv[count]);
			sum += atoi(argv[count]);
		}
		printf("sum = %d\n", sum);
	}
	else
	{
		printf("The command had no other argument\n");
	}
	return (0);
}
	

