a = int(input("Enter a positive integer: "))
try:
    if a <= 0:
        raise ValueError("Not a positive number!\n")
    print("you entered", a, "\n")
except ValueError as ve:
    print(ve)
