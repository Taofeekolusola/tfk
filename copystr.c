#include <stdio.h>
int copyString(char *str1, char *str2)
{
	while (*str1 !='\0')
	{
		*str1 = *str2;
		str1++;
		str2++;
	}
	*str2 = '\0';
}
int main()
{
	char str1[] = " Programming is a good skill";
	char str2[50];

	copyString(str1, str2);
	printf("str2: %s\n", str2);

	return (0);
}

