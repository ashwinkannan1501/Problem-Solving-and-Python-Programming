# Python program to multiply two matrices using nested loops
a = [[1, 1], [2, 2]]
b = [[4, 4], [5, 5]]
c = [[0, 0], [0, 0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j] = a[i][j] + a[i][k] * b[k][j]
print(f'The matrix elements is : {c}')
