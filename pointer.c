#include <stdio.h>
int main()
{
	int *pc, c = 10;
	pc = &c;
	*pc = 25;
	c = 50;

	printf("the value of pc = %p\n", pc);
	printf("Address of c = %p\n", &c);
	printf("the value strored in pc = %d\n", *pc);
	printf("the value c = %d\n", c);

	return (0);
}
