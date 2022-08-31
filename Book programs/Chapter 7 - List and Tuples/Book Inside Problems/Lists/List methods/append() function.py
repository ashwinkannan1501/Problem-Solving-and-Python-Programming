# append() function
"""The append() function is used to appends or adds the element at the end of the list
SYNTAX : list.append(element)"""

list_elements = list(input("Enter the list elements : ").split(","))

# list elements before appending
print(f'List elements before appending : {list_elements}')

# list elements after appending
list_elements.append("reshma")
print(f'List elements after appending : {list_elements}')
