class my_iter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            num = self.num
            self.num += 1
            return num
        else:
            raise StopIteration

it = my_iter()
print(next(it))
for i in it:
    print(i)
