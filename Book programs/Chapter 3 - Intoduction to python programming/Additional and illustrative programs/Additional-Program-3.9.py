# Python Program that accepts  an integer (n) and computes the value of n+nn+nnn
# Import the 'math' module to do the mathematical calculations
from math import pow
number = float(input("Enter a random number : "))
number_square = pow(number, 2)
number_cube = pow(number, 3)
print(f'Number: {number} \nSquare of a number({number}): {number_square} \nCube of a number({number}) : {number_cube}')
print(f'The addition of {number} + {number_square} + {number_cube} is {number + number_square + number_cube}')
