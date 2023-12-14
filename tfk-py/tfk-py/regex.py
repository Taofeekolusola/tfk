import re

re.search("ape", "there is an ape")
print("there is an ape")

theApe = "the ape is at the apex"
for i in re.finditer("ape.", theApe):
    locT = i.span()
    print(locT)
    print(theApe[locT[0]:locT[1]])
