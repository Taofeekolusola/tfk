#include <stdio.h>

int main()
{
	int arr[] = {45, 23, 99, 24, 56, 76, 34, 12, 14};
	int size = sizeof(arr) / sizeof(int);
	for (int i = 0; i < size; i++)
	{
		printf("Before Sorting");
		printf("%d", arr[i]);\
		printf("\n");
	}

	int i, j, temp;

	for (i = 0; i < size-1; i++)
	{
		for (j = 0; j < size-1; j++)
		{
			if (arr[j] < arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	for (i = 0; i < size; i++)
	{
		printf("After Sorting");
		printf("%d\n", arr[i]);
	}
}
