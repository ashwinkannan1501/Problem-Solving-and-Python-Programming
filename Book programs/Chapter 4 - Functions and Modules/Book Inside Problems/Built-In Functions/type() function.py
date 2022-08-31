# Python type() function
"""The type() function is used to return the type of that particular data
SYNTAX : type(object)"""
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))

# Printing list elements
print(f'The list elements are : {list_elements}')

# Printing the data type of the elements
print(f'The data type is : {type(list_elements)}')
