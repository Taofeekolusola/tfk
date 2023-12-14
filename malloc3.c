#include <stdio.h>
#include <stdlib.h>
int me(int a, int b, int c)
{
	int *n;
	int sum;

	n = (int *)malloc(sizeof(int) *3);
	if (n == NULL)
	{
		printf("Error! no memory was allocated");
	}

	n[0] = a;
	n[1] = b;
	n[2] = c;
	sum = a + b + c;
	printf("%d+%d+%d = %d\n", a, b, c, sum);
	free(n);
}
int main()
{
	me(500, 600, 700);
	return (0);
}
