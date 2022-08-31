# extend() function
"""The extend() function is used to extends the new list to an already existing list at a last
SYNTAX : list.extend(list_2)"""

list_elements = list(input("Enter the list elements : ").split(","))
extended_list = list(input("Enter the list elements that you want to extends : ").split(","))

# Original list
print(f'Before extending (original list) : {list_elements}')

# After extending a list
list_elements.extend(extended_list)
print(f'After extending a list : {list_elements}')
