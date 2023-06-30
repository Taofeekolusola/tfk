/**
#include <stdio.h>
void learn()
{
	printf("Learn C programming\n");
}
int main () {
	learn();
	learn();
	learn();
	return (0);
}

#include <stdio.h>
void calculateSquare(int number)
{
	int square = number * number;
	printf("the square of %d is %d\n", number, square);
}
int main()
{
	calculateSquare(6);
	return (0);
}
*/
/**
#include <stdio.h>
int add_number(int num1, int num2)
{
	int sum = num1 + num2;
	
       return (sum);
}
int main()
{
	int result = add_number(10,20);
	printf("result = %d\n", result);
	return (0);
}
*/
#include <stdio.h>
int multiply_numbers(int num1, int num2)
{
	int sum = num1 * num2;
	return (sum);
}
int main()
{
	int result = multiply_numbers(5,20);
		printf("result = %d\n", result);
	return (0);
}
