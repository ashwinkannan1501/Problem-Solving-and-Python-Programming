# Python program to convert a tuple into a string
tuple_elements = input('Enter the tuple elements : ')
tuple_elements = tuple(tuple_elements.split(","))
print(f"Tuple elements are : {tuple_elements}")
print(f'The data type of the elements is : {type(tuple_elements)}')

# Converting a tuple into string
string_elements = str(tuple_elements)
print(f'The string elements are : {string_elements}')
print(f'The data type of the elements is : {type(string_elements)}')
