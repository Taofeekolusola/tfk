def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result
fib_num = int(input("How many fibonacci number do you want: "))

i = 1

while i < fib_num:
    fibVal = fib(i)
    print(fibVal)

    i += 1

print("ALL Done")

