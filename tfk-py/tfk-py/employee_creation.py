class Employee:
    def __init__(self, name, age, salary, email):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
        print(f"Email: {self.email}")
        print()

def main():
    employees = []

    while True:
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            email = input("Enter email address: ")

            employee = Employee(name, age, salary, email)
            employees.append(employee)
            print("Employee added successfully!\n")

        elif choice == '2':
            if not employees:
                print("No employees to display.\n")
            else:
                print("Employee Information:")
                for employee in employees:
                    employee.display_info()

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
