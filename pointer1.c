#include <stdio.h>
int main()
{
	int x[3] = {1, 2, 3};

	for (int i = 0; i < 3; i++)
	{
		printf("&x[%d] = %p\n", i, &x[i]);
		printf("&x[%d] = %d\n", i, x[i]);
	}

	printf("Address of the first element x = %p\n", x);

	return (0);
}
