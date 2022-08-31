# Python program to find the sum of cosine series
# Import the 'math' module to do the mathematical calculations
from math import cos


def cosine_series(number):
    total = 0
    for i in range(1, int(cos(number + 1)), 1):
        total += 1 / i  # (or) total = total + (1/i)
    print(f'The sum of series when a number of terms({number}) is : {total}')


number = float(input("Enter a number : "))
cosine_number = cos(number)
cosine_series(number)
