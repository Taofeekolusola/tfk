def fun(*args):
    sum = 0
    for a in args:
        sum += a
    return sum
print(fun(1,2,3,4,5))

def fun1(arg1, arg2, arg3):
    print("arg1", arg1)
    print("arg2", arg2)
    print("arg3", arg3)

args = ("two", 2, 4)
print(fun1(*args))
kwargs = {"arg1": 5, "arg2": "two", "arg3": "Taofeek"}
print(fun1(**kwargs))
