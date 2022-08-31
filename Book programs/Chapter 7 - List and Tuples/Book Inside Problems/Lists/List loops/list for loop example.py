# list for loop example 1
# Python program to print the cubes of all numbers from 1 through 5

from math import pow
for index in range(1, 6):
    print(f'The cube of {index} is : {pow(index, 3)}')
