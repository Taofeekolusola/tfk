#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	int count = 0;

	while (count < argc)
		{
			if (argc > 1)
			{
				printf("argv[%d] = %s\n", count, argv[count]);
			}
			else
			{
				printf("the program does not have another argument\n");
			}
			count += 1;
		}
	return (0);
}
