/**
#include <stdio.h>
int main(void)
{
	int i;

	for (i = 0; i <= 5; i++)
	{
	if (i == 4)
	{
	break;
	}
	printf("\n%d", i);
	}
}
*/
#include <stdio.h>
int main(void)
{
	while (1)
	{int number;
	printf("Enter the number: ");
	scanf("%d", &number);
	if (number < 0)
	{ 
		break;
	}
	if ((number % 2) != 0)
	{
		continue;
	}
	printf("%d\n", number);
	}
}

/**
#include <stdio.h>
int main(void)
{
	for (int i = 0; i <= 10; i++)
	{
		if (i == 4)
		{
		continue;
		}
		printf("%d\n", i);
	}
}
*/
