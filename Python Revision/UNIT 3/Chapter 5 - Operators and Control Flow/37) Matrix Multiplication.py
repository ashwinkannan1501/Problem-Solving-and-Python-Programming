# Matrix Multiplication

a = [[56, 26], [89, 98]]
b = [[39, 56], [78, 59]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j] = a[i][j] + a[i][k] * b[k][j]

print(c)
