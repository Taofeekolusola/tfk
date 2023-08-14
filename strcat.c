#include <stdio.h>
#include <string.h>
int main()
{
	char str1[15] = "Taofeek";
	char str2[15] = "olusola";

	strcat(str1, str2);

	puts(str2);
	puts(str1);

	return (0);
}
