words = input("Convert to acronym: ")

words = words.upper()

words = words.split()

for w in words:
    print(w[0], end="")
print()
