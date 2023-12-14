pos = 1
def search(list, n):
    s = 0
    b = len(list)-1
    while s <= b:
        mid = (s+b) // 2
        if list[mid] == n:
            #get position
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                s = mid+1
            else:
                b = mid-1

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 19

if search(num, n):
    print("found at ", pos+1)
else:
    print("not found")
