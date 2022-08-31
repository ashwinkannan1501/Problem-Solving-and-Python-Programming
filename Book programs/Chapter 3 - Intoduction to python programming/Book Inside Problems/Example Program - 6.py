# EXPRESSIONS
from math import pi, pow
length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
radius = int(input("Enter the radius : "))
print(f'The area of the length({length}) and breadth({breadth})is {length * breadth}')
print(f'The area of the circle is : {pi * pow(radius, 2)}')
print(f'The area of the perimeter is : {2 * (length + breadth)}')
