m1 = [[3,0,4,-4], [5,10,-4,3], [5,5,2,0], [8,7,6,-4]]
m2 = [[5,3,2,0], [10,-2,-8,4], [3,5,1,1], [9,0,3,3]]

print(m1)
print(m2)

r = []
for i in range(4):
    r.append([])
    for j in range(4):
        r[i].append(m1[i][j]+m2[i][j])
print(r)
