#include <stdio.h>
int printScore(int scr[])
{
	printf(" MATHS: %d\n ENG: %d\n F.MATHS: %d\n PHY: %d\n", scr[0], scr[1], scr[2], scr[3]);
}
int main()
{
	int arrScr[4] = {78, 89, 95, 87};

	printScore(arrScr);

	return (0);
}
