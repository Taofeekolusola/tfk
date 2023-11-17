tree_height = int(input("How tall is the tree: "))
space = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
    for i in range(space):
        print(' ',end="")
    for i in range(hashes):
        print("#",end="")
    print()
    space -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
        print(' ',end="")
print("#")
