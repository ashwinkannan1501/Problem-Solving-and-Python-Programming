# Python program to compute the area of a circle
# Import the math module to do the mathematical operations
from math import pi, pow
radius = float(input("Enter the radius : "))
area_of_a_circle = (pi*(pow(radius, 2)))
print(f'Area of a circle is : {area_of_a_circle}')
