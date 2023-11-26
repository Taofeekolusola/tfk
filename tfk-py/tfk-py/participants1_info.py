class Participant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")

def main():
    participants = []  # Changed variable name to plural for clarity
    while True:
        print("1: Create new participant")
        print("2: Display participants")
        print("3: Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter participant name: ")
            age = int(input("Enter participant age: "))
            height = float(input("Enter participant height: "))
            if age < 10 or age > 20:
                print("you are not eligible to participate (15 - 20 years is eligible)")
                break
            elif height > 10.0:
                print("you are not eligible to participate (height 10 and below is eligible)")
                break
            part = Participant(name, age, height)
            participants.append(part)
            print("Participant info added successfully\n")

        elif choice == '2':
            if not participants:
                print("No participants added\n")
            for part in participants:
                part.display()

        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid choice, please enter a valid choice between 1-3")

if __name__ == "__main__":
    main()
