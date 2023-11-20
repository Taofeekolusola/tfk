def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def get_prime(max_num):
    l_num = []
    for num in range(2, max_num):
        if is_prime(num):
            l_num.append(num)
    return l_num
max_num = int(input("Search prime up to: "))

list_of_num = get_prime(max_num)

for prime in list_of_num:
    print(prime)
