#include <stdio.h>

int main()
{
	int var = 30; /* actual variable declaration */

	int *ip;  /* pointer variable declaration */

	*ip = &var; /* store address of var in a pointer variable */

	printf("Address of var variable: %ls\n", &var);

	printf("Address of ip variable: %ls\n", ip);

	printf("Value of *ip variable: %d\n", *ip);

	return (0);
}
