# List indexing
"""The list indexing means the position of the elements. Positive index starts from 0.
Negative index starts from -1. """

list_elements = list(input("Enter the list elements : ").split(","))
print(f'List elements : {list_elements[::]}')
print(f'List elements in reverse direction : {list_elements[::-1]}')
print(f'List elements from index 0 to 3 : {list_elements[:4]}')