#include <stdio.h>
#include <string.h>
int main()
{
	char str1[10] = "Taofeek";
	char str2[10] = "olusola";
	char str3[10] = "Adeshina";

	strcpy(str1, str2);
	strcpy(str2, str1);
	strcpy(str1, str3);
	
	puts(str1);
	puts(str2);
	puts(str3);

	return (0);
}
