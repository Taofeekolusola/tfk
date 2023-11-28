def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return sum(fib_sequence)

# Calculate the sum of the first 50 Fibonacci numbers
n = 50
result = fibonacci_sum(n)

print(f"The sum of the first {n} Fibonacci numbers is: {result}")
