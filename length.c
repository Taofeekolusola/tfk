#include <stdio.h>

int main()
{
	int length, data[5] = {1, 2, 3, 4, 5};

	length = sizeof data / sizeof data[0];

	printf("the length of the array is %d\n", length);

}
