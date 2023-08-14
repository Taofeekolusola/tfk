#include <stdio.h>
#include <stdlib.h>
char printName(char str[])
{
	printf("Name: ");
	puts(str);
}
int main()
{
	char str[20] = "Olusola Taofeek";

	printName(str);

	return (0);
}
