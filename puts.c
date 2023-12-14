#include <stdio.h>
#include "main.h"
int my_puts(const char *s)
{
	int i = 0;
	int sum;

	while (s[i] != '\0')
	{
		sum = my_putchar(s[i]);
		i++;
	}
	my_putchar('\n');
	return (sum);
}
