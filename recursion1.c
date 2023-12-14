#include <stdio.h>
int sumdigit(int num)
{
	if (num == 0)
		return (0);
	return (num % 10) + sumdigit(num / 10);
}
int main(void)
{
	int sum = sumdigit(530);
	printf("the sumdigit is %i\n", sum);
}
