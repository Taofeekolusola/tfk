def num_two(num):

    def two_times(val):
        return num * val
    return two_times

generated_val = num_two(4)
print("4 * 5 =", generated_val(5))
