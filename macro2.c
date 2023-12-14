#include <stdio.h>
#define VER 3
int main()
{
#if VER >=1 
	printf("This is version one\n");
#endif
#if VER >=2
	printf("This is version two\n");
#endif
#if VER >=3
	printf("This is version three\n");
#endif
}
