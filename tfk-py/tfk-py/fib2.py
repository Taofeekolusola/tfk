def fib(n):
    fib_num = [0, 1]

    for i in range(2, n):
        fib_num.append(fib_num[i-1] + fib_num[i-2])
    return fib_num

def print_fib(n):
    fib_num = fib(n)

    for i in fib_num:
        print(i)

print_fib(int(input("Enter the fibonacci number to find: ")))

print("End of list")
