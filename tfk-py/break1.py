sum = 0
while True:
    n = input("Enter a number: ")
    n = float(n)

    if n < 0:
        break
    sum += n
    print("sum =", sum)


