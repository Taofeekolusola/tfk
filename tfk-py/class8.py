class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def personality(self):
        print('My name is ', self.name, 'and i am', self.age, 'years old')

person1 = person('Olusola Taofeek', 30)
person2 = person('OLanipekun Ibrahim', 28)

person1.personality()
person2.personality()
