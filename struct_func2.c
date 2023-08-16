#include <stdio.h>
typedef struct Complex
{
	double real;
	double imag;
}Complex;
Complex AddNumber(Complex c1, Complex c2, Complex *sum)
{
	sum->real = c1.real + c2.real;
	sum->imag = c1.imag + c2.imag;
}
int main()
{
	Complex c1 = {2.5, 3.5}, c2 = {3.4, 6.3};

	Complex result;
	AddNumber(c1,c2,&result);

	printf("result.real = %.1lf\nresult.imag = %.1lf\n", result.real, result.imag);

	return (0);
}
