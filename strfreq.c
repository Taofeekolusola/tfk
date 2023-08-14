#include <stdio.h>
#include <string.h>
int main()
{
	char str[] = "life is good, but hereafter is the best";

	int i, freq = 0;
	char ch = 'e';

	for (i = 0; str[i] != '\0'; i++)
	{
		if (str[i] == ch)
		{
			freq++;

		}
	}
		printf("the frequency of %c is %d\n", ch, freq);

		return (0);
}
