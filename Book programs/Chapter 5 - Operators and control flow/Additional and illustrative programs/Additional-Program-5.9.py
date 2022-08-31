# Python program to find the multiplication table
print("--------------Multiplication Table -------------------")
n = int(input("Enter the n value : "))
i = int(input("Enter the i value : "))
for i in range(0, i+1, 1):
    print(f'{n} x {i} = {n*i}')
