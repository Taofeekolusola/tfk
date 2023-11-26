class Robot:
    def __init__(self, name, year, strg = 0.5, powr = 0.5):
        self.name = name
        self.year = year
        self.__strg = strg
        self.__powr = powr
    @property
    def condition(self):
        a = self.__strg + self.__powr
        if a < 0:
            return "i am very weak"
        elif a == 0:
           return  "i am weak"
        elif a <= 0.5:
           return  "it could be worse"
        elif a == 1:
           return "seems to be okay"
        else:
            return "i am in a good condition"
if __name__ == "__main__":
    T = Robot("Aburo", 2002, 0.7, 0.3)
    K = Robot("Dupe", 2001, -0.3, 0.3)
    print(T.condition)
    print(K.condition)
