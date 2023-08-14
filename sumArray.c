/**
#include <stdio.h>
int main()
{
	int x[10] = {12, 15, 23, 34, 45, 32, 21, 24, 54, 33};
	int sum = 0;
	int i, average;
	
	for (i = 0; i < 10; i++)
	{
		sum += x[i];
		average = sum / 10;
		printf("When the sum is %d\n", sum);
		printf("The average is %d\n", average);
	}

	return (0);
}
*/
#include <stdio.h>
int calsum(int sal[])
{
	int i, sum = 0.0;

	for (i = 0; i < 4; i++)
	{
		sum += sal[i];
	}

	return sum;
}
int main()
{
	int result, sal[4] = {12.2, 10.3, 15.5, 23.0};

	result = calsum(sal);
	printf("the sum is %d\n", result);
}
