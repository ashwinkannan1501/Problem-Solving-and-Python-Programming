# Fruitful function - The fruitful function has a return value
# Fruitful function example
"""Python program to print square of a number using fruitful function"""
from math import pow


def square_of_number(number):
    return f'The square of {number} is {pow(number, 2)}'


number = int(input("Enter a random number : "))
print(square_of_number(number=number))