from array import *

vals = array('i', [])

n = int(input("Enter the length of the array "))

for i in range(n):
    x = int(input("Enter the next number "))
    vals.append(x)
for i in vals:
    print(i)

arr = int(input("Enter value to search "))
k = 0
for e in vals:
    if e==arr:
        print(k)
else:
    print("Number not found")

    k+=1
