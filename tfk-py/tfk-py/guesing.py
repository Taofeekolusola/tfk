while (1):
    num = 5
    guess = int(input("Guess the number: "))
    if guess < num:
        print("Too small!! enter a higher number")
    elif guess > num:
        print("Too high!!! enter a smaller number")
    else:
        print("Congratulations you guessed correctly")
        break
