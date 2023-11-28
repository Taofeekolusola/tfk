import random

def generate_binary_number(length):
    binary_number = ''.join(random.choice('01') for _ in range(length))
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

# Generate a random binary number with 4 digits
binary_number = generate_binary_number(4)

# Convert the binary number to base 10
decimal_number = binary_to_decimal(binary_number)

# Display the results
print(f"Generated Binary Number: {binary_number}")
print(f"Equivalent Decimal Number: {decimal_number}")
