def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def is_primes(max_num):
    list_of_primes = []

    for num1 in range(2, max_num):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes

max_num1 = int(input("Search for primes up to : "))

list_of_primes = is_primes(max_num1)

for prime in list_of_primes:
    print(prime)
