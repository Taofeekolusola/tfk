#include <stdio.h>
struct person
{
	char name[50];
	int age;
};
void print(struct person person1)
{
	printf("name: %s\n", person1.name);
	printf("age: %d\n", person1.age);
}
int main()
{
	struct person person1 = {"Taofeek", 32};

	print(person1);

	return (0);
}
