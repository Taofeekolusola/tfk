#include <stdio.h>
typedef struct Complex
{
	double real;
	double imag;
}Complex;
Complex addNumber(Complex c1, Complex c2)
{
	Complex sum;
	sum.real = c1.real + c2.real;
	sum.imag = c1.imag + c2.imag;

	return (sum);
}
int main()
{
	Complex c1 = {12.5, 15.4}, c2 = {13.3, 14.5};
	Complex result;

	result = addNumber(c1,c2);
	printf("result.real = %.1lf\nresult.imag = %.1lf\n", result.real, result.imag);

	return (0);
}
