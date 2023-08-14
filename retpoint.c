#include <stdio.h>
int* addtwenty(int* num)
{
	for (int i = 0; i < 5; i++)
	{
		*(num + i) = *(num + i) + 20;
	}

	return num;
}
int main()
{
	int num[5] = {1, 2, 3, 4, 5};
	int *result;
	
	result = addtwenty(num);

	for (int i = 0; i < 5; i++)
	{
		printf("%d\n", *(result + i));
	}

	return 0;
}
