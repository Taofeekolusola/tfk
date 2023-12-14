#include <stdio.h>
#include <string.h>

int main()
{
	const char *name = "My name is %s ";
	const char *surname = "Olusola\n";

	printf(name, "Taofeek");
	printf("%s", surname);

	return 0;
}
