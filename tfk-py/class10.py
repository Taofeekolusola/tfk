class store:
    def __init__(self, name, loc, price):
        self.name = name
        self.loc = loc
        self.price = price
        self.out = self.outlet

    def show(self):
        print(self.name, self.loc, self.price)
        self.out.show

    class outlet:
        def __init__(self):
            self.goods = clothes
            self.quantity = 500

        def show(self):
            print(self.goods, self.quantity)

s1 = store('Taofeek', 'Lagos', 100)
s2 = store('Olusola', 'Abuja', 200)

s1.show()
s2.show()
