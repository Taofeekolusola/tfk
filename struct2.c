#include <stdio.h>

struct member
{
	char name[50];
	int age;
	int contribution;
};
int main()
{
	struct member member1 = {.name = "Olusola Taofeek", .age = 30, .contribution = 100000};
	struct member member2 = {.name = "Mustapha Ibrahim", .age = 29, .contribution = 200000};
	struct member member3 = {.name = "Olanipekun Ibrahim", .age = 35, .contribution = 300000};

	printf("Member1's name: %s\n", member1.name);
	printf("Member1's age: %d\n", member1.age);
	printf("Member1's contribution: %d\n", member1.contribution);
	printf("Member2's name: %s\n", member2.name);
	printf("Member2's age: %d\n", member2.age);
	printf("Member2's contribution: %d\n", member2.contribution);
	printf("Member3's name: %s\n", member3.name);
	printf("Member3's age: %d\n", member3.age);
	printf("Member3's contribution: %d\n", member3.contribution);

	return (0);
}
