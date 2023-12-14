from numpy import *

arr = array([1,2,3,4,5])
arr1 = array([1,2,3,4,5])
arr2 = arr.copy()
arr3 = arr1.view()

arr[0] = 10
arr[0] = 10

print(id(arr))
print(id(arr2))
print(id(arr1))
print(id(arr3))

print(arr)
print(arr2)
print(arr1)
print(arr3)
