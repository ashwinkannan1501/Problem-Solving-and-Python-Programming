"""Python function program to create and print the list where the values are square of numbers
between 1 and 30 (both included)"""
from math import pow


def values():
    list_values = []
    for i in range(1, 31, 1):
        list_values.append(pow(i, 2))
    print(list_values)


values()
