def sol_x(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " +  str(num2 - num1)
print(sol_x("x + 4 = 9"))
