# List comprehension example

from math import pow
list_comprehension = [pow(number, 2) for number in range(1, 7)]
print(f'List comprehension = {list_comprehension}')
