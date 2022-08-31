# Python program to solve (x+y)*(x+y)
# Import the 'math' module to do the mathematical calculations
from math import pow
x = float(input("Enter the X value : "))
y = float(input("Enter the Y value : "))
print(f'({x}+{y})*({x}+{y}) = {pow((x+y), 2)}')
