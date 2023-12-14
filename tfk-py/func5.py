a = 10
def fun():
    a = 9
    x = globals()['a']
    a = 10
    print(a)
    globals()['a'] = 15
fun()

print(a)
