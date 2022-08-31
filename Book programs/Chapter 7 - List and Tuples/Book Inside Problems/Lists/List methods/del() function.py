# del() function
"""TYhe del() function is used to deletes the elements with the index if provided
SYNTAX : del(index)"""

list_elements = list(input("Enter the list elements : ").split(","))
delete_element = int(input("Enter the index element that you want to delete : "))

# original list
print(f'Original list : {list_elements}')

# deleted list elements
del list_elements[delete_element]
print(f'List elements after deleting : {list_elements}')
