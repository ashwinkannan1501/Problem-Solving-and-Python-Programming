# Python Program to calculate the factorial of a number (non-negative integer)
from math import factorial


def fact(number):
    if(number == 1) or (number == 2):
        return number
    else:
        return number * fact(number - 1)


number = int(input("Enter a number : "))

# Calculate the factorial of a number with using built-in math 'factorial()' function
print(f'The factorial of {number} is : {factorial(number)}')

# Calculate the factorial of a number without using built-in math 'factorial()' function
print(f'The factorial of {number} is : {fact(number)}')
