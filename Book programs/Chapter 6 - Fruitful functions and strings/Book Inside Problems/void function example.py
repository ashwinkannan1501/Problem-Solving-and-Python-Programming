# Void function - It does no have the return value
"""Python program to print square of a number using void function"""

from math import pow


def square_of_number(number):
    print(f'The square of {number} is : {pow(number, 2)}')


number = int(input("Enter a random number : "))

square_of_number(number=number)