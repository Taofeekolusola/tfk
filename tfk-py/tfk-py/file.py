import os

with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("My name is Taofeek\nI am 30 years old\n i live in Lagos\n")


with open("mydata.txt", encoding="utf-8") as myfile:
 """  print(myfile. readlines())
   print(myfile.mode)
   print(myfile.name)
   print(myfile.closed)

os.rename("myfile.txt", "mydata.txt")
os.remove("mydata.txt")
#3os.mkdir("mydir")
# os.chdir("mydir")
print("Current Working Directory", os.getcwd())
# os.chdir("..")
#os.rmdir("mydir")
print("Current Working Directory", os.getcwd())"""

with open("mydata.txt", encoding="utf-8") as myfile:
    lineNum = 1
    
    while True:
        line = myfile.readline()
        if not line:
            break
        print("Line", lineNum, " : ", line,  end="")
        lineNum += 1
