class fibNum:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fibnum = self.first + self.second
        self.first = self.second
        self.second = fibnum
        return fibnum

fib = fibNum()
for i in range(5):
    print("fib = ", next(fib))
