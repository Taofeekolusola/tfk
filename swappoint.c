#include <stdio.h>
void swapval(int *n1, int *n2)
{
	//use temp to swap the values of *n1 and *n2
	int temp;
	temp = *n1;
	*n1 = *n2;
	*n2 = temp;
	return;
}
int main()
{
	int num1 = 1;
	int num2 = 10;

	printf("%d\n%d\n", num1, num2);

	swapval(&num1, &num2);

	printf("%d\n%d\n", num1, num2);

	return (0);
}
