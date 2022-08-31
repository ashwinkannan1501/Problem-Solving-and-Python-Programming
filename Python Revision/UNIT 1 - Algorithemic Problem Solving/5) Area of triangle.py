# Area of triangle given all the three sides algorithm

import math

a = int(input("Enter the a value : "))
b = int(input("Enter the b value : "))
c = int(input("Enter the c value : "))

s = (a + b + c) / 2

d = (s * (s - a) * (s - b)* (s - c))

area_of_triangle = math.sqrt(d)

print(f"Area of triangle of sides {a}, {b}, {c} is : {area_of_triangle}")
