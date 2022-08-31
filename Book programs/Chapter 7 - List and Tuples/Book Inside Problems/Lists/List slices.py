# List slices
"""List slicing means printing the specific element in the list by specifying the index"""

list_elements = list(input("Enter the list elements : ").split(","))

print(f'Printing an entire list in forward direction: {list_elements[::]}')
print(f'Printing an entire list in reverse direction : {list_elements[::-1]}')
print(f'Printing an element in the 0th index : {list_elements[0]}')
print(f'Printing an element in the 1st index : {list_elements[1]}')
print(f'Printing an element in the list form 1 to 3 : {list_elements[1:4]}')
print(f'Printing an element in the list form 1 to 3 and steps to 2: {list_elements[1:4:2]}')
