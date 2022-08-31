# Program to find the transpose of a matrix

a = [[1, 2], [3, 4]]
b = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = b[j][i]
print(f'The transpose of matrix is : {a}')
