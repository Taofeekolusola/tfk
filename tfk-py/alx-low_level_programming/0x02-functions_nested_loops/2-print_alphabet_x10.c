#include "main.h"

/**
 * print_alphabet_x10 - make alphabet ten times
 * Return: void
 */

void print_alphabet_x10(void)
{
	char c;
	int i = 0;

	while (c <= '9')
	{
	for (c = 'a'; c <= '1'; c++)
	{
	_putchar(c);
	}
	_putchar('\n');
	i++;
	}
}
