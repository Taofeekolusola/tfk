#include <stdio.h>
int cyclicSwap(int *a, int *b, int *c)
{

	int temp;

	temp = *b;
	*b = *a;
	*a = *c;
	*c = temp;
}
int main()
{
	int a = 3, b = 4, c = 5;

	cyclicSwap(&a, &b, &c);

	printf("The value after function call\n");
	printf("a = %d\nb = %d\nc = %d\n", a, b, c);

	return 0;
}
