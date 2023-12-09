multilist = [[1,2,3],
             [4,5,6],
             [7,8,9]]
print([col[1] for col in multilist])
print([multilist[i][i] for i in range(len(multilist))])
print([col[2] for col in multilist])
