

butts = [[1,2,3,1], [1,1,1,True]]
for i, row in enumerate(butts):
    butts[i] = [elem for elem in row if elem != True]
    print(row)
