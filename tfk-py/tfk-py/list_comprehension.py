print([x * 2 for x in range(1, 11)])
print([x for x in range(1, 11) if x % 2 == 0])
print([x ** 2 for x in range(50) if x % 8 == 0])
print([x * y for x in range(1, 3) for y in range(10, 13)])
print([x  for x in [i * 2 for i in range(10)] if x % 8 == 0])
