from array import *

vals = array('i', [1, 2, 3, 4, 5])

val1 = array(vals.typecode, (a for a in vals))

for i in range(len(val1)):
    print(val1[i])
print(vals.typecode)
