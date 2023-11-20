def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

num = 3.14
print(isfloat(num))
