import random
import math
numlist = []
for i in range(10):
    numlist.append(random.randrange(1, 15))
for i in numlist:
    print(i)

i = len(numlist)-1

while i > 1:
    j = 0
    while j < i:
        print("{} > {}".format(numlist[j], numlist[j + 1]))
        if numlist[j] > numlist[j + 1]:
            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j + 1] = temp
            print("Switch")
        else:
            print("Don't Switch")
        j += 1

    i -= 1
for k in numlist:
    print(k, end=", ")
print()
