import os

with open("myfile.txt", mode="w", encoding="utf") as myfile:
    myfile.write("Today is Saturday\nThis is weekend\nPeople rest at home\n")

with open("myfile.txt", encoding="utf-8") as myfile:

    while 1:
        
        lineNum = 1
        line = myfile.readline()
        if not line:
            break

        wordCount = line.split()

        size = len(wordCount)
        count = 0

        for word in wordCount:
            for char in word:
                count += 1
                print(char)
