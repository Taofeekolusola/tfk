class Big:
    def pick(self):
        print("first item")
        print("second item")
        print("third item")

class small:
    def picks(self, item):
        item.pick()

item = Big()
a1 = small()
a1.picks(item)
