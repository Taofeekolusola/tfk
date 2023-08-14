#include <stdio.h>
#include <string.h>
int main()
{
	char str1[] = "welcome";
	char str2[] = "goodbye";

	printf("the length of str1 is: %lu\n", strlen(str1));
	printf("the length of str2 is: %zu\n", strlen(str1));

	return (0);
}
