#include <stdio.h>
struct person
{
	char name[50];
	int age;
	double salary;
}; 
int main()
{
	struct person person1;

	printf("Enter name: ");
	fgets(person1.name, sizeof(person1.name), stdin);

	printf("Enter age: ");
	scanf("%d", &person1.age);

	printf("Enter Salary: ");
	scanf("%lf", &person1.salary);

	printf("Name: %s\n", person1.name);
	printf("Age: %d\n", person1.age);
	printf("Salary: %lf", person1.salary);

	return (0);
}
