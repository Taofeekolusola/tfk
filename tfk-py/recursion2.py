import sys
sys.getrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print("hello", i)
    greet()
greet()

