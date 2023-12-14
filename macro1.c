#include <stdio.h>
#define ADD(X)  (X+X)

int main()
{
	int a = ADD(2) * ADD(3);
	printf("%d/n", a);
}
