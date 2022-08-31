# Python code to demonstrate the working of pow() and sqrt()
# Import the 'math' module to do the mathematical calculations
from math import pow, sqrt
base = int(input('Enter the base number : '))
exponent = int(input("Enter the exponent number : "))

# The 'pow()' function behaves like base^exponent(eg. 2^2). It has two parameters.1) base 2) exponent
print(f'The base({base}) to power({exponent}) is : {pow(base, exponent)}')

number = int(input("Enter a number : "))

# The sqrt() function behave like a square root of a number
print(f'The square root of a number ({number}) is : {sqrt(number)}')
