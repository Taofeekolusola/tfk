def func(list2, fun):
    oddlist = []

    for i in list2:
        if fun(i):
            oddlist.append(i)

    return oddlist

def isOdd(num):
    if (num % 2) == 0:
        return False
    else:
        return True

list1 = [1,2,3,4,5]

print(func(list1, isOdd))
