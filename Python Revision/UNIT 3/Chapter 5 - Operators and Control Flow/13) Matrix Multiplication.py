# Python program to multiply two matrices using nested loops

a = [[9, 18], [1, 1]]
b = [[2, 2], [3, 3]]
c = [[0, 0], [0, 0]]

for i in range(0, len(a), 1):
    for j in range(0, len(b), 1):
        for k in range(0, len(b), 1):
            c[i][j] = a[i][j] + a[i][k] * c[k][j]

print(c)
    
