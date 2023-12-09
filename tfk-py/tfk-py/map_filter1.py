print(list(map((lambda x, y: x + y), [2,4,6], [2,4,6])))
print(list(map((lambda x: x % 2), [10, 11, 23, 34])))
print(list(filter((lambda x: x % 2 != 0), range(1, 20))))
