def sumAll(*args):
    sum = 0

    for i in args:
        sum += i
    return sum

print("Sum: ", sumAll(1,10,12,20,33,43,12,13,5,52,67))
