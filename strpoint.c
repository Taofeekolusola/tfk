#include <stdio.h>
#include <stdlib.h>
int main()
{
	char name[] = "Taafeek";
	
	printf("%c\n", *name);
	printf("%c\n", *(name + 1));
	printf("%c\n", *(name + 6));

}
