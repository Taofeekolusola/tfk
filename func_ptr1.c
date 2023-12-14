#include <stdio.h>
int multi(int a, int b)
{
	return (a*b);
}
int main()
{
	int (*multi_ptr)(int, int) = &multi;
	int result = (*multi_ptr)(10, 10);

	printf("result = %d\n", result);
	return (0);
}
