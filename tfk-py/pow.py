import math

numlist = [1,2,3,4,5]

listOfVal = [[math.pow(m, 1), math.pow(m, 2), math.pow(m, 3), math.pow(m, 4), math.pow(m, 5)] for m in numlist]
for i in listOfVal:
    print(i)
