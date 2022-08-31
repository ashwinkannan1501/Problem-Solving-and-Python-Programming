# python program to print the '*' using nested for loop

maximum_stars = int(input("Enter a maximum stars : "))

for i in range(1, maximum_stars + 1):
    print("*" * i)
    
for j in range(maximum_stars - 1, 0, -1):
    print("*" * j)
