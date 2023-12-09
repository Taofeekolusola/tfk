import random
randlist = list(random.randint(1, 1001) for i in range(100))

alist = list(filter((lambda x: x % 9 == 0), randlist))

print(alist)
