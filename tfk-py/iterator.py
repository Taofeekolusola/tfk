class infIter:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num

i = infIter()
a = iter(i)
for i in infIter():
    print(i)
    if i == 100:
        break
