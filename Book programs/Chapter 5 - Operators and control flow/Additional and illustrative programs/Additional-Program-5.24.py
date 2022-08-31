# Python program to find the area of a circle
# Import th 'math' module to do the mathematical calculations
from math import pi, pow
radius = int(input("Enter the radius of a circle : "))
print(f'The area of a a circle when radius ({radius}) is : {pi*pow(radius, 2)}')
