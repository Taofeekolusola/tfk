#include <stdio.h>
#include <stdlib.h>

/**
 * Ptr: the pointer
 * i: ilterator
 */

int main()
{
	int *ptr, i;

	//allocate memory

	ptr = (int *)malloc(2 * sizeof(int));

	//print the memory space

	printf("Previous memory\n");
	for (i = 0; i < 2; i++)
	printf("%p\n", ptr + i);

	//reallocate memory
	
	ptr = (int *)realloc(ptr, 4 * sizeof(int));
       	
	//print the current memory space
	
	printf("Current memory\n");
	for (i = 0; i < 4; i++)
	printf("%p\n", ptr + i);

	//deallocate memory
	free(ptr);

	return (0);
}
