class me:
    def __init__(self, myn, mys):
        self.myname = myn
        self.mysurname = mys
    def printname(self):
        print(self.myname, self.mysurname)
x = me("Olusola", "Taofeek")

class me1(me):
    def __init__(self, myn, mys, age):
        super().__init__(myn, mys)
        self.age = age
    def name(self):
        print("My name is", self.myname, self.mysurname, "and i am", self.age, "years old")
x = me1("Olusola", "Taofeek", 50)
x.name()
