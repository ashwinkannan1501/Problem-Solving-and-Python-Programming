# remove() function
"""The remove() function is used to removes the specified element provided in the argument
SYNTAX : list.remove(element)"""

list_elements = list(input("Enter the list elements : ").split(","))

# Before removing an element from the list
print(f'Before removing an element from the list : {list_elements}')

# After removing an element from the list
list_elements.remove("kirthika")
print(f'After removing an element from the list : {list_elements}')
