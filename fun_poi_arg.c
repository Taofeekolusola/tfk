#include <stdio.h>
int fun1(int a, int b)
{
	return (a + b);
}
int fun2(int a, int b)
{
	return (a * b);
}
int wrapper(int (*fun)(int, int))
{
	int a = 10, b = 20;
	int result = fun(a, b);
	printf("%d\n", result);
	return (0);
}

int main()
{
	wrapper(fun1);
	wrapper(fun2);
	return (0);
}
