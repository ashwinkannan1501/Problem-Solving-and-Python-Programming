# Python Program to compute the distance between the two points (X1, Y1) and (X2, Y2)
# Import the 'math' module to do the mathematical calculations
from math import sqrt, pow
x1 = float(input("Enter the x1 value : "))
y1 = float(input("Enter the y1 value : "))
x2 = float(input("Enter the x2 value : "))
y2 = float(input("Enter the y2 value : "))
distance_between_two_points = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))
print(f'Distance between {x1}, {y1}, {x2}, {y2} is : {distance_between_two_points}')
