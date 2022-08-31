""" Python program to generate and print a list of first and last 5 elements where the values are
square of numbers between 1 and 20 (both included)"""
# Import the 'math' module to do the mathematical calculations
from math import pow
new_list_elements = []
for list_elements in range(1, 21):
    new_list_elements.append(pow(list_elements, 2))
print(f"The square of list elements : {new_list_elements}")
print(f'The square of list elements from 1 to 5 : {new_list_elements[:5]}')
print(f"The square of list elements from 16 to 20 : {new_list_elements[-5:]}")
