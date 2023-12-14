def is_odd(x):
    return x%2!=0
num = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10, 11]

output = list(filter(is_odd, num))
print(output)
