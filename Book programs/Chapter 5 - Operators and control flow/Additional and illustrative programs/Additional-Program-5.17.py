# Python program to print the "*" using nested for loop
a = int(input('Enter the value : '))
for i in range(1, a+1):
    print("*" * i)
    for j in range(a, 0, -1):
        print("*" * j)
