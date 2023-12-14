from numpy import *

arr = array ([
                [1,2,3,10,11,12],
                
                [4,5,6,7,8,9]

                        ])

arr1 = arr.flatten()
arr2 = arr1.reshape(2,2,3)
print(arr2.ndim)
print(arr.dtype)
print(arr1.size)
print(arr2)
