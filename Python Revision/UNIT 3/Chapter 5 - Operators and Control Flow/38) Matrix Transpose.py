# Matrix Transpose

a = [[5, 10], [8, 6]]
b = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        a[i][j] = b[j][i]

print(a)
