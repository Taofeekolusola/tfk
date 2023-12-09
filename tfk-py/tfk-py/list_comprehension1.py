import random

print([x for x in [random.randrange(1, 1001) for i in range(50)] if x % 9 == 0])
