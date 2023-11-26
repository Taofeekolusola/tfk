class building:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    @property
    def length(self):
        print("Retrieving the length")

        return self.__length
    
    @length.setter
    def length(self, value):
        if value.isdigit():
            self.__length = value
        else:
            print("please only enter numbers for length")


    @property
    def breath(self):
        print("Retrieving the breath")

        return self.__breath

    @breath.setter
    def breath(self, value):
        if value.isdigit():
            self.__breath = value
        else:
            print("please only enter numbers for breath")
    def getArea(self):
        return int(self.__length) * int(self.__breath)

def main():
    length = input("Enter the length of the building: ")
    breath = input("Enter the breath of the building: ")
    abuild = building(length, breath)

    abuild.length = length
    abuild.breath = breath
    
    print("Length", abuild.length)
    print("Breath", abuild.breath)

    print("Area of the building", abuild.getArea())
main()

if __name__ == "__main__":
    main()
