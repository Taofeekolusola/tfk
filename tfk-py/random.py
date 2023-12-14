import random

randlist = list(random.randint(1, 100) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), randlist)))
