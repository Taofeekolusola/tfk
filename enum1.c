#include <stdio.h>
enum traffic
{
	green,
	red,
	yellow,
	blue
};
int main()
{
	enum traffic light;
	light = red;

	switch (light) 
	{
		case green:
		printf("GO\n");
		break;

		case red:
		printf("STOP\n");
		break;

		case yellow:
		printf("READY TO GO\n");
		break;

		default:
		printf("Not recognized\n");
	}

	return (0);
}
