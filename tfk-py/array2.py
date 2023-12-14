from array import *
vals = array('i', [1, 2, 3, 4, 5])
newArr = array('i', (a+a for a in vals))
i = 0
while i<len(newArr):
    print(newArr[i])
    i+=1
