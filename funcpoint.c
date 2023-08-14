#include <stdio.h>
void changeNum(int *n)
{
	*n = 100;

	return;
}
int main()
{
	int num = 10;
	
	printf("%d\n", num);

	changeNum(&num);
	printf("%d\n", num);

	return (0);
}
