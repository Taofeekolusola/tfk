#include <stdio.h>

struct person
{
	double salary;
	int age;
};
int main()
{
	struct person *personPtr, person1;

	person1.age = 35;
	person1.salary = 99000.000000;

	personPtr = &person1;

	printf("salary: %.2lf\n", personPtr->salary);
	printf("age: %d\n", personPtr->age);
	printf("address: %p\n", personPtr);

	return (0);
}
