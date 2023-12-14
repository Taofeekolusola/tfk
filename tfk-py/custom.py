class CustomError(Exceptions):
    "Base class for other exceptions"
    pass

class ValueTooSmallError(Error):
    "raised when the input value is too small"
    pass

class ValueTooHighError(Error):
    "raised when the input value is too high"
    pass

number = 10

while True:
    try:
        num = int(input("Entera number: "))
        if num < number:
            raise
ValueTooSmallError

        elif num > number:
            raise
ValueTooHighError
        break

    except ValueTooSmallError:
        print("This value is too small, try again")

    except ValueTooHighError:
        print("This value is too high, try again")

 print("you guessed correctly. :) ")
