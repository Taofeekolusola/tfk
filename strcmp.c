#include <stdio.h>
#include <string.h>
int main()
{
	char str1[10] = "Cool";
	char str2[10] = "bool";
	int result;

	result = strcmp(str1, str2);

	if (result == 0)
	{
		printf("The strings are equal\n");
	}
	else
	{
		printf("the strings are not equal\n");
	}

	return (0);
}
