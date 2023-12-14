def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = input("Enter the values you wish to count")
even, odd = count(lst)
print(even)
print(odd)
