#include <stdio.h>
struct person
{
	char name[50];
	int age;
       double salary;
};
int main()
{
	struct person person1 =  {.name = "Taofeek", .age =30, .salary = 300000.00};

	printf("name: %s\n", person1.name);
	printf("age: %d\n", person1.age);
	printf("salary: %.2lf\n", person1.salary);

	struct person person2 =  {.name = "Olusola", .age =35, .salary = 350000.00};

	printf("name: %s\n", person2.name);
	printf("age: %d\n", person2.age);
	printf("salary: %.2lf\n", person2.salary);

	return (0);
}
	
