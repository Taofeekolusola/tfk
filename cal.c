#include <stdio.h>

int main()
{
	char operator;

	printf("Enter the operator ['+', '-', '*', '/',]");
	scanf("%c", &operator);
	
	double num1, num2;

	printf("Enter the first number: ");
	scanf("%lf", &num1);

	printf("Enter the second number: ");
	scanf("%lf", &num2);
	
	double result;

	switch (operator) 
	{
	case '+':
	result = num1 + num2;
	break;

	case '-':
	result = num1 - num2;
	break;

	case '*':
	result = num1 * num2;
	break;
	
	case '/':
	result = num1 / num2;
	break;
	}
	return (result);
}
