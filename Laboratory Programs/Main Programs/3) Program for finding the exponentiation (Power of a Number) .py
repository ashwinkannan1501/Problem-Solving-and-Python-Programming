# Python program for finding the exponentiation (Power of a number)
# Import the necessary module
from math import pow

base_number = int(input("Enter the base number : "))
exponent_number = int(input("Enter the exponent number : "))

print(f'The base ({base_number}) to the power of exponent ({exponent_number}) is : {pow(base_number, exponent_number)}')
