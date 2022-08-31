# List mutability
"""Mutability means changing an element after instantiating"""

list_elements = list(input("Enter the list elements : ").split(","))
changing_element = input("Enter the element : ")
index = int(input("Enter the index of the element : "))

# Original lists
print(f'Original lists : {list_elements}')

# Mutability lists
list_elements[index] = changing_element
print(f'Mutability lists : {list_elements}')
