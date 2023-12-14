class arithmetic:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def __lt__(self,other):
        a1 = self.a1 < other.a1
        a2 = self.a2 < other.a2
        if a1 < a2:
            return True
        else:
            return False

b1 = arithmetic(15, 17)
b2 = arithmetic(15, 19)
if b2 < b1:
    print("win")
else:
    print("lose")
