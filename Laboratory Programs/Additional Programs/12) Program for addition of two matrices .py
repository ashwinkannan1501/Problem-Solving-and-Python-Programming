# Program for addition of two matrices

a = [[1, 2], [3, 4]]
b = [[5, 6],  [7, 8]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] + b[i][j]
print(f'The addition of {a} and {b} matrix is : {c}')
