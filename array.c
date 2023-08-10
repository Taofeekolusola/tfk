#include <stdio.h>

int main()
{
	//delear an integer
	int i, data[5];

	//collect data from the audience
	printf("Enter five numbers: ");
	for (i = 0; i <  5; i++)
	scanf("%d", &data[i]);

	printf("Array elements are: ");
	for (i = 0; i < 5; i++)
	printf("%d ", data[i]);

	return (0);
}
