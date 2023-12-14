#include <stdio.h>
#define PI 3.1415
int main()
{
	float radius, area;
	printf("Enter the radius");
	scanf("%f", &radius);

	area = PI * radius * radius;
	printf("area = %.2f\n", area);

	return (0);
}
