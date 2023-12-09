def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def gen_even(max_num):
    for num1 in range(max_num):
        if is_prime(num1):
            yield num1
even = gen_even(20)
for i in even:
    print(i)
