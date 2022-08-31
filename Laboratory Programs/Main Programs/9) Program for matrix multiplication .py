# Program for matrix multiplication

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j] = a[i][k] * b[k][j] + c[i][j]
            print(c[i][j])
            break
