custom = []
while True:
    makeEntry = input("Enter customer (yes/no): ")
    makeEntry = makeEntry[0].lower()
    if makeEntry == "n":
        break
    else:
        fName, lName = input("Enter customer name: ").split()
        custom.append({"fName": fName, "lName": lName})
for c in custom:
    print(c['fName'], c['lName'])
