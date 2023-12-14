from numpy import *

arr = array([  [1,2,3,4,5,11],
            
                [6,7,8,9,10,12]

                ])

arr1 = arr.flatten()
arr2 = arr1.reshape(3,4)
arr3 = arr2.reshape(2,2,3)
print(arr)
print(arr)
print(arr2)
print(arr.size)
print(arr1.ndim)
print(arr2.dtype)
print(sum(arr2))
print(arr3)
