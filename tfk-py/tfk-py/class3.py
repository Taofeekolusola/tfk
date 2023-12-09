class Life:
    def __init__(self, name, age):
        self.name = name
        self._age = int(age)  # Convert age to an integer

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if self._age >= 60:
            self._age = val
        else:
            print("You still have a long life to live")

    def age_status(self):
        if self._age >= 80:
            print("You are too old and you can die anytime")
        elif  self._age <= 50 and self._age < 80:
            print("You are getting old. Please make hay while the sun shines.")
        else:
            print("You still seem to have age on your side, but never relent. Keep striving and don't be too confident. you can die at anytime.")

def main():
    life1 = Life("wiwe", 75)
    life1.age_status()
    life2 = Life("Sise", 50)
    life2.age_status()
    life3 = Life("kilo", 80)
    life3.age_status()

if __name__ == "__main__":
    main()
