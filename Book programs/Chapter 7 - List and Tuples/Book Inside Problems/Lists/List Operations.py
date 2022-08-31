# List Operators

# Creating two list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

# Concatenation operator (+)
print(f'The concatenation of {list_1} and {list_2} is : {list_1 + list_2}')

# Repetition operator (*)
print(f'The repetition of {list_1} by 3 times is : {list_1 * 3}')

# len() function
print(f'The length of {list_1} is : {len(list_1)}')

# min() and max() function
print(f'The minimum of {list_1} is ; {min(list_1)}')
print(f'The maximum of {list_1} is : {max(list_1)}')

# Membership Operator ("in" and "not in")
print(f'The list_1 ({list_1}) in list_2 ({list_2}) is : {list_1 in list_2}')
print(f'The list_1 ({list_1}) not in list_2 ({list_2}) is : {list_1 not in list_2}')

# list() function
tuple_element = ("ashwin", "kannan", "amutha")
print(f'Converting the elements from tuple data type ({tuple_element}) to list data type is : {list(tuple_element)}')
