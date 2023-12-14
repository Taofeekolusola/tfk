numlist = [[0] * 5 for i in range(5)]

for i in range(5):
    for j in range(5):
        numlist[i][j] = "{} : {}".format(i, j)

for i in range(5):
    for j in range(5):
        print(numlist[i][j], end=" || ")
    print()
