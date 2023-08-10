#include <stdio.h>

int main()
{
	int week;

	printf("Enter a number between 1 - 7: ");
	scanf("%d", &week);

	switch (week)
	{
		case 1 :
		printf("Today is Sunday\n");
		break;

		case 2 :
		printf("Today is Monday");
		break;

		case 3 :
		printf("Today is Tuesday\n");
		break;

		case 4 :
		printf("Today is Wednessday\n");
		break;

		case 5 :
		printf("Today is Thursday\n");
		break;

		case 6 :
		printf("Today is Friday\n");
		break;

		case 7 :
		printf("Today is Saturday\n");
		break;

		default :
		printf("Enter a valid number between 1 - 7\n");
	}
}
