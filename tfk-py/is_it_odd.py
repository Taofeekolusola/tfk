def is_it_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def change_list(lists, func):
    
    oddlist = []
    
    for i in lists:
        
        if func(i):

            oddlist.append(i)
    return oddlist

lists = range(1, 20)
print(change_list(lists, is_it_odd))
