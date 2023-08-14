#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i, n, *scores;

	// obtain number from the user

	printf("Enter a random number: ");
	scanf("%d", &n);

	// allocate memory space for the scores

	scores = (int *)malloc(n * sizeof(int));

	// return NULL if malloc fails

	if (scores == NULL)
	{
		printf("Error! memory not allocated");
	}
	// obtain scores from the audience

	printf("Enter the scores: ");
	for (i  = 0; i < n; i++)
	scanf("%d", scores + i);

	//print the scores obtained

	for (i = 0; i < n; i++)
	printf("The scores obtained is: %d\n", *(scores + i));

	//deallocate space memory

	free(scores);
	 return (0);
}
