# Python code to demonstrate the working of exp() and log()
# Import the 'math' module to do the mathematical operations
from math import exp, expm1, frexp, ldexp, log, log1p, log2, log10
base = int(input('Enter the base number : '))
exponent = int(input("Enter the exponent number : "))
print(f'The base number({base}) to the power of exponent ({exponent}) is : {exp(base)}')

number = int(input("Enter the number : "))
print(f'log = {log(number, base)}')
print(f'log2 = {log2(number)}')
print(f'log10 = {log10(number)}')
print(f'log1p = {log1p(number)}')
