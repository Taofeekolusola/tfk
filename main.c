#include <stdio.h>
#include "main.h"

int main()
{
	void (*p)(char *);

	p = &printHello;

	(*p)("ibragaza");
	 return (0);
}

