#include <stdio.h>
struct Employee
{
	int age;
	double salary;
}person[3];
int main()
{
	for (int i = 0; i < 3; i++)
	{
		printf("for employee %d\n", i + 1);
		printf("Enter age: ");
		scanf("%d", &(person + i)->age);

		printf("Enter salary: ");
		scanf("%lf", &(person + i)->salary);
	}

	for (int i = 0; i < 3; i++)
	{
		printf("For employee %d\n", i + 1);
		printf("age: %d\n", (person + i)-> age);
		printf("salary: %lf\n", (person + i)->salary);
	}

	return (0);
}
