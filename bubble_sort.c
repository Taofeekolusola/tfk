#include <stdio.h>

int main()
{
	int arr[] = {12, 34, 53, 13, 19, 21};
	int size = sizeof(arr) / sizeof(int);
	
	int i, j, temp, swap = 0, pass;
	printf("Before Sorting: ");
	printf("\n");
	for (i = 0; i < size; i++)
	{
		printf("%d\n", arr[i]);
	}

	for (i = 0; i < size - 1; i++)
	{
		for (j = 0; j < size - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
				swap = 1;
			}
		}
		pass++;

		if (swap == 0)
		{
			break;
		}
	}
	printf("%d\n", pass);

	printf("After sorting: \n");
	for (i = 0; i < size; i++)
	{
		printf("%d\n", arr[i]);
	}
}
