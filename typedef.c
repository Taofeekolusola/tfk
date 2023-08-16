#include <stdio.h>

typedef struct scores
{
	int maths;
	int fmaths;
}scores;

int main()
{
	scores s1 = {.maths = 56, .fmaths = 45};
	scores s2 = {.maths = 25, .fmaths = 23};

	scores sum;

	sum.maths = s1.maths + s2.maths;
	sum.fmaths = s1.fmaths + s2.fmaths;

	printf("Sum maths = %d\nsum fmaths = %d\n", sum.maths, sum.fmaths);

	return (0);
}
