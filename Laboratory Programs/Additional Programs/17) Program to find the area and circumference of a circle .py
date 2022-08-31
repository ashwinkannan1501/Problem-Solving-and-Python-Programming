# Program to find teh area and circumference of a circle

from math import pi

radius = int(input("Enter the radius : "))

area_of_a_circle = (pi * radius * radius)
circumference_of_a_circle = 2 * pi * radius

print(f'The area of a circle is : {area_of_a_circle}')
print(f'The circumference of a circle is : {circumference_of_a_circle}')
