def findReciprocal(value):
    try:
        print("value:", value, "\n")
        r = 1/value
        print("the reciprocal of", value, "is", r, "\n")
    except:
        print("you cannot find the reciprocal of", value,"\n")
findReciprocal("Hello")
findReciprocal(2)
