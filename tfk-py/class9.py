class person:
    def __init__(self):
        self.name = 'Taofeek'
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

p1 = person()
p2 = person()

p1.age = 25

if p1.compare(p2):
    print("they are same")
else:
    print("they are diff")
