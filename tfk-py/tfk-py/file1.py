import os

with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("Coding is life\nit's fun to code\n you learn a lot through hardwork\nbut you make it by Allah's grace\n")

with open("mydata.txt", encoding="utf-8") as myfile:

    lineNum = 1

    while 1:

        lineSize= len(myfile.readline())
        line = myfile.readline()

        if not line:
            break
        print("Line", lineNum)

        WordList = line.split()
        print("Number of words", len(WordList))

        chaCount = 0

        for word in WordList:
            for char in word:
                chaCount += 1
        avrNum = chaCount/len(WordList)

        print("Avr word Length is {}".format(avrNum))
        lineNum += 1
