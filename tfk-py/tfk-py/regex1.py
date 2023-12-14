import re
animalStr = "rat cat mat dat fat"

allAn = re.findall("[rcmdf]at", animalStr)

for i in allAn:
    print(i)
allAn1 = re.findall("[c-fC-M]at", animalStr)
for i in allAn1:
    print(i)
allAn2 = re.findall("^Cf]at", animalStr)
for i in allAn2:
    print(i)
