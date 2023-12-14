pos = 1
def search(list, n):
    i = 0
    while i< len(list):
        if list[i] == n:
            #get position
            globals()['pos'] = i
            return True
        i = i + 1
    return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 1

if search(nums, a):
    print("found at ", pos+1)
else:
    print("not found")
