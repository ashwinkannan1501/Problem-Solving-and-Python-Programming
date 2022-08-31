# 25) Python program to find the square root of a number

number = int(input("Enter a number : "))

# Without using 'sqrt()' function
square_root = number ** 0.5

print(f"The square root of {number} is : {square_root}")

# With using 'sqrt()' function
from math import sqrt

print(f"Square root of {number} using 'sqrt()' function : {sqrt(number)}")


