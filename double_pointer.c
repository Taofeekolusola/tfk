#include <stdio.h>

int main()
{
	int a = 30;
	int **p;
	*p = &a;
	**p = 50;

	printf("%p\n", *p);
	printf("%d\n", **p);
	return (0);
}
