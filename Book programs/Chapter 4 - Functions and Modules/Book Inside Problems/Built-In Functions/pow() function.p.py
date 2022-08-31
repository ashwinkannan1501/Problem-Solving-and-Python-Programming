# Python pow() function
"""The pow() function is used to find the power of a value. It returns x to the power of y.
If the third argument (z) is given, it returns x to the power of y modulus z (i.e) pow(x, y) % z.
The pow() function is equivalent to (x ** y).
SYNTAX : pow(x, y [, z])
         where x - Number which is to be powered
               y - Number which is to be powered with x
               z (optional) - Number which is to be used for modulus operation"""
from math import pow
x = int(input("Enter the x value : "))
y = int(input("Enter the y value : "))
# z = int(input("Enter the z value : "))
print(f'The power of x and y without using math built-in "pow()" function  is : {x ** y}')
print(f'The power of x and y with using math built-in "pow()" function  is : {pow(x, y)}')
