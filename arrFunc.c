#include <stdio.h>

int printSalary(int sal1, int sal2)
{

	printf("%d\n%d\n", sal1, sal2);

	return (0);
}
int main()
{
	int salArray[4] = {40000, 50000, 60000, 70000};
	
	int result = printSalary(salArray[1], salArray[3]);

	return (0);
}	
