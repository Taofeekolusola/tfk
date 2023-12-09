class set_get:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x <= 0:
            self.__x = 0
        elif x >= 1000:
            self.__x = 1000
        else:
            self.__x = x

set1 = set_get(10)
print(set1.x(10))
set2 = set_get(1001)
print(set2.x(1001))
set3 = set_get(-1)
print(set3.x(-1))
