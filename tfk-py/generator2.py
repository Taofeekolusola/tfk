def top_twenty():

    i = 1
    while i <= 20:
        sq = i*i
        yield sq
        i += 1

s1 = top_twenty()
for i in s1:
    print(i)
