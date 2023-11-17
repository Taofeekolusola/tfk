#enter the number to be calculated
num1, num2 = input("Enter two number ").split()
#choose the opeartor of your choice
operator = input("Choose an operator between: +, -, *, / ")
#convert the numbers into integers
num1 = int(num1)
num2 = int(num2)
#declare sum
sum = num1 + num2
#declare mul
mul = num1 * num2
#declare div
div = num1 / num2
#declare sub
sub = num1 - num2

if operator == "+":
    print("{} + {} = {}".format(num1, num2, sum))
elif operator == "*":
        print("{} * {} = {}".format(num1, num2, mul))
elif operator == "/":
        print("{} / {} = {}".format(num1, num2, div))
elif operator == "-":
        print("{} - {} = {}".format(num1, num2, sub))
else:
    print("invalid operator")
