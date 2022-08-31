# Matrix Subtraction

a = [[4, 5], [8, 12]]
b = [[8, 15], [26, 33]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] - b[i][j]


print(c)
