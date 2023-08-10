#include <stdio.h>
int main()
{
	int guess, num = 30;

	while (1)
	{

	printf("Enter a number between 1-50: ");
	scanf("%d", &guess);


	if (num > guess)
	{
		printf("Wrong! please enter a higher number\n");
	}
	else if (num < guess)
	{
		printf("wrong! enter a lower number\n");
	}
	else
	{
		printf("Congratulations you are correct\n");
		break;
	}
	}

	return (0);
}
