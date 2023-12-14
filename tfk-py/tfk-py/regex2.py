import re

Eatable = "rat mat cat bat"

regex = re.compile("[c-r]at")

Eatable = regex.sub("eat", Eatable)
print(Eatable)

backSl = "this is \\stuff"

print("find \\stuff", re.search(r"\\stuff", backSl))
