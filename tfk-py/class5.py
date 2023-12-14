class MyClass:
    def __init__(self, p1 = 1, p2 = 2):
        self.a = p1
        self.b = p2
a1 = MyClass(3, 4)
print(a1.a, a1.b)
a2 = MyClass()
print(a2.a, a2.b)
class MyClass:
    a = 2
    def func(self):
        print ('Hello')
a1 = MyClass()
print(a1.a)
print(a1.func())
