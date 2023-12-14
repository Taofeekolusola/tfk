def cal_rec(n):
    if n == 1:
        return 1
    else:
        return n + cal_rec(n-1)
sum = cal_rec(4)
print(sum)
