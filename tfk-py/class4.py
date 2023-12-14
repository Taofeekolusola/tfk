class MyClass:
    def __init__(self, a1 = 1, a2 = 2):
        self.a = a1
        self.b = a2

k1 = MyClass(22, 30)
print((k1.a, k1.b))

k2 = MyClass(15, 20)
print((k2.a, k2.b))

k3 = MyClass()
print((k3.a, k3.b))
