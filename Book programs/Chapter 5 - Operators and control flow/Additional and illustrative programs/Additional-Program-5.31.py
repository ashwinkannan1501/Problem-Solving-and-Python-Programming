# python program to find the sum of sine series
# Import the 'math' module to do the mathematical calculation
from math import sin


def sine(sine_value):
    total = 0
    for i in range(1, int(sin(number + 1)), 1):
        total += 1 / i  # (or) total = total + (1/i)
    print(f'The sum of series when a number of terms({number}) is : {total}')


number = int(input("Enter a number : "))
sine_value = sin(number)
sine(sine_value)
