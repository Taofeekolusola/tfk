#include "main.h"

/**
 * _puts - Prints a stringe
 * @str: The string to be printed
 * Return: void
 */

void _puts(char *str)
{
	for (; *str != '\0'; str++)
	{
	_putchar(*str);
	}
	_putchar('\n');
}
