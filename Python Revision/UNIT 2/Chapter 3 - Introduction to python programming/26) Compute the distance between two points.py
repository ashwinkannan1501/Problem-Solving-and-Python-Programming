# Python program to compute the distance between two points (x1, y1) and (x2, y2)

import math  # Import the "math" module

# Get the x1, y1, x2, y2 value from the user
x1 = int(input("Enter the x1 value : "))
y1 = int(input("Enter the y1 value : "))

x2 = int(input("Enter the x2 value : "))
y2 = int(input("Enter the y2 value : "))

distance = math.sqrt(
    ((x2 - x1) ** 2) + ((y2 - y1) ** 2))  # Calculate the distance between 2 points by using the formula

print(f"Distance between {x1}, {x2}, {y1}, {y2} is : {distance}")  # Print the result
