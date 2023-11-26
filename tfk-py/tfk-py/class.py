class house:
    def __init__(self, name, style, location):
        self.name = name
        self.style = style
        self.location = location

    def tall(self):
        print("{} the house is tall".format(self.name))
        print("the house is {}".format(self.style))
        print("the house is in {} ".format(self.location))

    def beautiful(self):
        print("{} the house is beautiful".format(self.name))
        print("the house is {}".format(self.style))
        print("the house is in {} ".format(self.location))

def main():
    king = house("King", "Modern", "Abuja" )
    king.tall()
    king.beautiful()

    Royal = house("Royal", "old", "Lekki")
    Royal.tall()
    Royal.beautiful()



main()
