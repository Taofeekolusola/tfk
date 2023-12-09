def fun1(num):
    def fun2(val):
        return num * val
    return fun2

generated_val = fun1(10)

print("10 * 10 = ", generated_val(10))
