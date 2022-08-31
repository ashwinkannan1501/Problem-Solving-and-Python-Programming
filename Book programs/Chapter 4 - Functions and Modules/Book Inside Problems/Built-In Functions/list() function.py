# Python list() function
"""The list() function is used to create a list in python
SYNTAX : list(object)
         where object should be string, tuple, set, dictionary"""
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))
print(f'List elements are : {list_elements}')