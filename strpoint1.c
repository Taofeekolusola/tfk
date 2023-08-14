#include <stdio.h>
int main()
{
	char *ptrname;
	ptrname = "olusola";

	printf("%c\n", *ptrname);
	printf("%c\n", *(ptrname + 1));
	printf("%c\n", *(ptrname + 2));
	printf("%c\n", *(ptrname + 3));
	printf("%c\n", *(ptrname + 4));
        printf("%c\n", *(ptrname + 5));
	printf("%c\n", *(ptrname + 6));

	return (0);
}
