import math
import time
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
        return True
t0 = time.time()
c = 0
for n in range(1, 100000):
    x = is_prime(n)
    c += x
print("The number of prime is", c)

t1 = time.time()
print("The amount of time required is", t1 - t0)
