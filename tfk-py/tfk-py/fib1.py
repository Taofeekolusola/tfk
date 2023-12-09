def fib(num):
    fib_num = [0, 1]

    for i in range(2, num):
        fib_num.append(fib_num[i-1] + fib_num[i-2])
    return fib_num

def print_fib_num(num):
    fib_seq = fib(num)
    for i in fib_seq:
        print(i)
print_fib_num(int(input("Enter the num you want to find: ")))

print("End of list")
