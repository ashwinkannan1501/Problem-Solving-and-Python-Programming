"""Python program to generate and print a list except for the first 5 elements, where the values
are square of numbers between 1 and 30 (both included)"""
from math import pow
new_list_elements = []
for list_elements in range(1, 31):
    new_list_elements.append(pow(list_elements, 2))
print(f"The square of list elements from 6 to 30 is :\n{new_list_elements[5:]}")
