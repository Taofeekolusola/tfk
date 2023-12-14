#include <stdio.h>
int main()
{
	int data[5] = {23, 12, 34, 21};
	
	printf("%d\n", *(data + 1));
	
	*(data + 2) = 50;

	printf("%d\n", *(data + 3));

	printf("%d\n", data[0]);

	printf("%d\n", *(data + 2));
	printf("%d\n", data [3]);

	printf("%d\n", *(data + 0));

	printf("%d\n", data[2]);

	return (0);
}	
