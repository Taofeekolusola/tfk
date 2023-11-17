while (1):
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("you didn't enter a number")
    except:
        print("you need to enter a number")
print("Thanks for entering a number")
