#include <stdarg.h>
#include <stdio.h>

int Addnum(int n, ...)
{
	int sum = 0;
	int i = 0;

	va_list next;

	va_start(next, n);

	while (i < n)
	{
		sum += va_arg(next, int);
		i++;
	}
	
	va_end(next);

	return (sum);
}

int main()
{
	int res = Addnum(3, 3,4,5);
	printf("res = %d\n", res);
	return (0);
}
