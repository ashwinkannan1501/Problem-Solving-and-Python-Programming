# Python program to find the sum of the series : 1 + x^2/2 + x^3/3 + .... + x^n/n

n = int(input("Enter the 'n' value : "))
x = int(input("Enter the 'x' value : "))

sum = 0

for i in range(1, n+1):
    sum += (x ** i)/i

print("The Sum of the series is : ", sum)
