#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	FILE *fo;
	
	fo = fopen("taofile.txt", "w");

	fprintf(fo, "%s", "Hello World");

	fclose(fo);

	return (0);
}
