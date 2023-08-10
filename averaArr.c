#include <stdio.h>
int main()
{
	double x[5] = {23.0, 25.4 -12.5, 13.3, 2.5};
	double sum = 0.0;

	for (int i = 0; i < 5; i++)
	sum += x[i];
	double average = sum / 5;

	printf("sum is %.2lf\n", sum);
	printf("average is %.2lf\n", average);

         return (0);
}
