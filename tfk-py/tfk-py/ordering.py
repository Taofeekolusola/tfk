import random
from datetime import datetime, timedelta

class Rider:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, client_name, destination):
        self.order_id = random.randint(1000, 9999)
        self.client_name = client_name
        self.destination = destination
        self.timestamp = datetime.now()
        self.status = "Pending"
        self.rider = None

def display_orders(orders):
    print("Orders:")
    for order in orders:
        print(
            f"Order ID: {order.order_id}, Client: {order.client_name}, Destination: {order.destination}, Status: {order.status}"
        )
    print()

def display_riders(riders):
    print("Available Riders:")
    for rider in riders:
        print(f"Rider: {rider.name}")
    print()

def assign_rider(order, riders):
    if not riders:
        print("No available riders.")
        return

    rider = random.choice(riders)
    order.rider = rider
    order.status = "Assigned"
    print(f"Order {order.order_id} assigned to {rider.name}.")

def main():
    riders = [Rider("Rider 1"), Rider("Rider 2"), Rider("Rider 3")]
    orders = []

    while True:
        print("1. Place Order")
        print("2. Display Orders")
        print("3. Display Available Riders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            client_name = input("Enter your name: ")
            destination = input("Enter the destination: ")
            order = Order(client_name, destination)
            orders.append(order)
            assign_rider(order, riders)

        elif choice == "2":
            display_orders(orders)

        elif choice == "3":
            display_riders(riders)

        elif choice == "4":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
