from array import *

val = array('i', [])

n = int(input("Enter the length of the array "))

for i in range(n):
    x = int(input("Enter the next value "))
    val.append(x)

for i in val:
    print(i)

y = int(input("Enter the number to search "))
a = 0
for e in val:
    if e==y:
        print(a)
        break
else: 
    print("number not found")
    a+=1

print(val.index(y))
