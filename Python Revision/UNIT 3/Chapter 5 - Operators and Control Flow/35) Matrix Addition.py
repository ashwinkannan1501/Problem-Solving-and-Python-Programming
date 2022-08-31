# Matrix Addition

a = [[1, 2], [5, 6]]
b = [[8, 10], [15, 12]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] + b[i][j]
        
print(c)
    
