#include <stdio.h>

int main(void)
{
	int num;
	printf("Enter a number: ");
	scanf("%d", &num);
	
	int count = 1;

	while (count <= 10)
	{
		int result = num * count;
		printf("%d*%d = %d\n", num, count, result);
		count = count + 1;
	}
	return (0);
}
