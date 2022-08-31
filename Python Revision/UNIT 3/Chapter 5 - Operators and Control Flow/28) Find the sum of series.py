# Python program to find the sum of the series : 1+ 1/2 + 1/3 + ..... + 1/n

n = int(input("Enter the 'n' value : "))

sum = 0

for index in range(1, n+1):
    sum += 1/index

print("The Sum of series is : ", sum)
