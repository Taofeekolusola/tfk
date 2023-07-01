#include <stdio.h>

int main()
{
	
		while (0) 
	{
		int num;

		printf("Enter a number: ");
		scanf("%d", &num);

		if (num > 0)
		{
			printf("Positive Number");
		break;
		}

		if (num < 0 && (num % 2) == 0)
		{
			printf("Negative Even");
		continue;
		}
		printf("%d", num);	
	}
		return (0);
}
