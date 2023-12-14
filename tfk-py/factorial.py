def fac(n):

    f = 1

    for i in range(1,n+1):
        f = f*i

    return f
result = fac(4)

print(result)
