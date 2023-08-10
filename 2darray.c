#include <stdio.h>
int main ()
{
	int x[4][5] = {{23, 34, 24, 45, 56}, {12, 13, 42, 31, 21}, {19, 13, 15, 61, 73}, {98, 56, 34, 65, 67}};

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			printf("%d \n", x[i][j]);
		}
	}

	return (0);
}
