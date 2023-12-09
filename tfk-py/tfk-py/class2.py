class life:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, val):
        if self.age >= 60:
            self.age = val
        else:
            print("you still have a long life to live")

    def age_status(self):
        if self.age >= 80:
            print("You are too old and you can die anytime")
        elif self.age >= 50 and self.age < 80:
            print("You are getting old please make hay while the sun shine")
        else:
            print("you still seem to have age on your side, but never relent keep striving and don't be too confident, age is different from daeth.")
def main():
    life1 = life("wiwe", "75")
    life1.age
    life1.age_status()
main()
