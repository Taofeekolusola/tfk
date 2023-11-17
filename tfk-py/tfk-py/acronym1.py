words = input("Enter the words to generate acronym: ")

word_list = words.split()

acronym = ''.join(w[0].upper() for w in word_list)
print(acronym)
