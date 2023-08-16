#include <stdio.h>
struct staff
{
	char name[50];
	int age;
	double salary;
}staff[3];
int main()
{
	//for loop to ilterate through 
	for (int i = 0; i < 3; i++)
	{
		//take name, age and salary of three staff
		printf("for staff %d: \n", i + 1);
		// get name of the user
		printf("Enter name: ");
		fgets(staff[i + 1].name, sizeof(staff[i + 1].name), stdin);

		//get age of the user
		printf("Enter age: ");
		scanf("%d", &staff[i].age);
		
		//get salary of the user
		printf("Enter salary: ");
		scanf("%lf", &staff[i].salary);
	}

		//print the name, age an salary of three staff

	for (int i = 0; i < 3; i++)
	{

		printf("Staff: %d\n", i + 1);

		printf("Name: %s\n", staff[i].name);

		printf("Age: %d\n", staff[i].age);

		printf("Salary: %lf\n", staff[i].salary);

	}

	return (0);
}
