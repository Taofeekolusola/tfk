for a in range(3):
    for i in range(4):
        for j in range(4-i):
            print("#",end="")
        print()

    for i in range(4):
        for j in range(i+1):
            print("#",end="")
        print()
    print()
