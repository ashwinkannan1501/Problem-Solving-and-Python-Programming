# Cloning list
"""Cloning is a process of making a copy of a list without modifying the original list.
Changes in one list will not affects the another list
Creating a copy of list of elements with two different memory locations is called cloning
cloning can be done by one of three methods
    1) Slicing
    2) list() function
    3) copy() function"""

list_elements = list(input("Enter the list elements : ").split(","))

# Slicing
cloning_list_elements_slicing = list_elements[:]

# list() function
cloning_list_elements_list_function = list(list_elements)

# copy() function
cloning_list_elements_copy_function = list_elements.copy()

# Modifying the list elements
list_elements[1] = "reshma"

# Printing the list elements
print(f'List elements : {list_elements}')
print(f'Cloning list elements using slicing : {cloning_list_elements_slicing}')
print(f'Cloning list elements using list() function : {cloning_list_elements_list_function}')
print(f'Cloning list elements using copy() function : {cloning_list_elements_copy_function}')
