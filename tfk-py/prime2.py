import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(1, n):
        if n % i == 0:
            return False
        return True
t0 = time.time()
c = 0
for n in range(1, 100000):
    x = is_prime(n)
    c += x
print("The total prime number is", c)
t1 = time.time()
print("Time required is:", t1 - t0)
