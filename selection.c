#include <stdio.h>

int main()
{
	int arr[] = {34, 23, 56, 77, 87, 12, 10, 29};
	int size = sizeof(arr) / sizeof(int);

	int i, j, temp;

	for (i = 1; i < size-1; i++)
	{
		int min = i;
		for (j = i + 1; j < size; j++)
		{
			if (arr[j] < arr[min])
			{
				min = j;
			}
		}
		if (min != i)
		{
			temp = arr[min];
			arr[min] = arr[i];
			arr[i] = temp;
		}
	}
	for (i = 0; i < size; i++)
	{
		printf("After Sorting");
		printf("%d", arr[i]);
		printf("\n");
	}
}
