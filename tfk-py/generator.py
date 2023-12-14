def my_gen():
    n = 1
    print("first")
    yield n

    n += 1
    print("second")
    yield n
    
    n += 1
    print("Third")
    yield n
for i in my_gen():
    print(i)
