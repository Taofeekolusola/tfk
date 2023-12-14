n = int(input("please enter the number you wish to check. between 1-100 "))
for i in range(2, n):
    if (n <= 1):
        print("False")
        break

    elif (n % i) == 0:
        print("Not prime")
        break
else:
    print("it's prime")
