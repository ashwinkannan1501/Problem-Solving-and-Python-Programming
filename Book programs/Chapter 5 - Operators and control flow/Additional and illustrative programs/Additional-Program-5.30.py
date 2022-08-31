# Python program tpo find the sum of series : 1 + x^2/2 + x^3/3 + x^n/n
# Import the 'math' module to do the mathematical calculations
from math import pow
number = int(input("Enter the number of elements : "))
x = int(input("Enter the x value : "))
total = 1
for i in range(2, number+1, 1):
    total += ((pow(x, i)) / i)  # (or) total = total + (x**i)/i
print(f'The sum of series when a number of terms({number}) is : {total}')
