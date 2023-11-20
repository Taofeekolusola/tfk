def sol_x(eq):
    num1, opr, x, equal, num2 = eq.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 / num1)
print(sol_x("4 * x = 8"))
