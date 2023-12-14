class person:
    def __init__(self, country, country2):
        self.Nigeria = country
        self.Ghana = country2
    def printcountry(self):
        print(self.Nigeria, self.Ghana)
x = person("Nigeria", "Ghana")
x.printcountry()
class person2(person):
    def __init__(self, country, country2):
        self.Nig = country
        self.Gha = country2
    def printstate(self):
        print(self.Nig, self.Gha)

x = person2("Ivory Coast", "Liberia")
x.printstate()
