#include <stdio.h>

void func(int a)
{
	printf("%d\n", a);
}
int main()
{
	void (*func_ptr)(int);
	func_ptr = func;
	func_ptr(20);
	return (0);
}
