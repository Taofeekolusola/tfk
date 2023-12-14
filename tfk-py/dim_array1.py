from array import *

val = array('i', [])
n = int(input("Enter the number of values "))

for i in range(n):
    x = int(input("Enter the next value "))
    val.append(x)

for i in val:
    print(i)

y = int(input("Enter the number to search"))

k = 0
for e in val:
    if y==e:
        print(k)
    k+=1
    break
else:
    print("Number not found")
