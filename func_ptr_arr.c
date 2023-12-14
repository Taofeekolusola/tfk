#include <stdio.h>

int add(int a, int b)
{
	int sum = a + b;
	return (sum);
}
int sub(int a, int b)
{
	int res = a / b;
	return (res);
}
int mul(int a, int b)
{
	int prod = a * b;
	return (prod);
}

int main()
{
	int (*fun_ptr_arr[])(int, int) = {add, sub, mul};
	int ch, a = 20, b = 10;

	printf("Enter a number between 0-2 where 0 adds 1 divides and 2 multiplies: ");
	scanf("%d", &ch);

	if (ch > 2) 
		return (0);
	int result = (*fun_ptr_arr[ch])(a, b);
	printf("%d\n", result);
	return (0);
}
