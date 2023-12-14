av = 5
shoes = int(input("How many shoes do you want?"))
i = 1
while i <= shoes:
    if av < i:
        print("currently out of stock")
        print("please order a lesser number")
        break

    print("shoe no ", i)
    i+=1
print("Bye")
