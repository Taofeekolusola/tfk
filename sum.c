#include <stdio.h>

int main(void)
{
	int sum = 0;

	for (int a = 1; a <= 100; a = a+3)
	{
	sum = sum + a;
	}
	printf("%d", sum);

	return (0);
}
