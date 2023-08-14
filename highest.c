#include <stdio.h>
#include <stdlib.h>

int main()
{
	//declearing the elements
	
	int elem[5] = {10, -20, 30, 15, 20};

	for (int i = 0; i < 5; i++)
	{
		if (elem[0] < elem[i])
		{
			elem[0] = elem[i];
			printf("%d is the highest number\n", elem[0]);
		}
	}

	return (0);
}
