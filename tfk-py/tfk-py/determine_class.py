age = eval(input("Enter your age: "))
if age < 5:
    print("you are not fit for school yet")
elif age == 5:
    print("Go to kindergarten")
elif age >= 6 and age <= 17:
    grade = age - 5
    print("Go to grsde {}".format(grade))
elif age >= 17:
    print("Go to college")
