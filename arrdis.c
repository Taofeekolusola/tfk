#include <stdio.h>
int displayArray(int n[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\n", n[i][j]);
		}
	}
}
int main()
{
	int result, data[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

	result = displayArray(data);

	return (0);
}
