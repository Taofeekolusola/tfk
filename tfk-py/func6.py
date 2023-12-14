def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = [31,21,34,42,45,46,76,77,23,21,44,49,50,40,54,78,70]
even, odd = count(lst)
print("Even :", even, "Odd :", odd)
