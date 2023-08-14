#include <stdio.h>
int main()
{
	char str[] = "taofeek olusola";
	int count = 0;
	
	while (str[count] != '\0')
	{

		count++;
	}

	printf("the length of str is: %d\n", count);

	return (0);
}
