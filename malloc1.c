#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, *A;
	int i = 0;

	A = (int*)malloc(n*sizeof(int));
	printf("Enter a number ");
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		A[i] = i + 1;
		printf("%d\n", A[i]);
	}
	if (A == NULL)
	{
		printf("Error memory was not allocated\n");
	}
	int *B = (int*)realloc(A, 2*n*sizeof(int));
	for (i = 0; i < n; i++)
	{
		B[i] = i + 1;
		printf("%d\n", B[i]);
	}

	return (0);
}
