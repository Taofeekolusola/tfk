tree = int(input("Enter tree size: "))
space = tree + 1
hashes = 1
s_space = tree + 1
while tree != 11:
    for i in range(space):
        print(' ',end="")
    for i in range(hashes):
        print("#",end="")
    print()
    space += 1
    hashes += 2
    tree += 1
for i in range(s_space):
    print(' ',end="")
print("#")
