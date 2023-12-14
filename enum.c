#include <stdio.h>
enum week
{
	sunday,
	monday,
	tuesday,
	wednesday,
	thursday,
	friday,
	saturday,
};
int main()
{
	enum week today;
	today = tuesday;

	printf("today is day %d\n", today + 1);

	return (0);
}
