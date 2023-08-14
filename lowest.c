#include <stdio.h>
#include <stdlib.h>

int main()
{
	int data[5] = {12, 13, 45, 56, 15};

	for (int i = 0; i < 5; i++)
	{
		if (data[0] > data[i])
		{
			data[0] = data[i];
			printf("%d is the lowest number\n", data[0]);
		}
	}

	return (0);
}
