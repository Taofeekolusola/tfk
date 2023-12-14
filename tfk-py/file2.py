with open("test.txt", 'r', encoding = 'utf-8') as f:
    f.read("My first file\n")
    f.read("My name is Taofeek\n")
    f.read("I am 20 years old\n")
print(f.read())
