# Python tuple() function
"""The tuple() function is used to create a tuple in python, In python, a tuple is an immutable
sequence type. It is most commonly used to typecasting from another data type to tuple data type.
SYNTAX : tuple(object)"""
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))

# Printing list elements
print(f'The list elements are : {list_elements}')
print(f'The data type is : {type(list_elements)}')

# Converting the elements from list data type to tuple data type
tuple_elements = tuple(list_elements)

# Printing the tuple elements
print(f'The tuple elements are : {tuple_elements}')
print(f'The data type is : {type(tuple_elements)}')
