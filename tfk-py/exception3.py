def divof(val):
    try:
        print("value is", val,'\n')
        v = val/2
        print("the half of", val, "is", v, '\n')

    except ValueError:
        print("Error you have a value error")
    except ZeroDivisionError:
        print("Zero Division error")
    finally:
        print("your code ran successfully")
divof(30)
divof(0)
divof(-1)
