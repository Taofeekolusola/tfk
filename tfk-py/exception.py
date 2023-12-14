def findReciprocal(value):
    try:
        print("value:", value, "\n")
        v = 1/value
        print("the reciprocal of", value, "is", v, "\n")
    except ValueError:
        print("you got value error\n")
    except ZeroDivisionError:
        print("you got zero division error\n")
findReciprocal(4)
findReciprocal(0)
findReciprocal(20)
