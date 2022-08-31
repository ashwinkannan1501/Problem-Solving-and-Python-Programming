# Tuple functions

# Creating a tuple
tuple_elements = tuple(input("Enter the tuple elements : ").split(","))

# index() function - Returns the index of the first matched item - SYNTAX : tuple.index(element)
print(f'index of "reshma" is : {tuple_elements.index("reshma")}')

# count() function - Returns the count of the given element - SYNTAX : tuple.count(element)
print(f'count of "reshma" is : {tuple_elements.count("reshma")}')

# len() function - Returns the length of the tuple - SYNTAX : len(tuple)
print(f'The length of the tuple elements ({tuple_elements} is : {len(tuple_elements)}')

# min() function - Returns a minimum element in a tuple - SYNTAX : min(tuple)
print(f'The minimum element in a tuple elements ({tuple_elements}) is : {min(tuple_elements)}')

# max() function - Returns a maximum element in a tuple - SYNTAX : max(tuple)
print(f'The maximum element in a tuple elements ({tuple_elements}) is : {max(tuple_elements)}')

# del() function - Deletes an entire tuple - SYNTAX : del(tuple)
del tuple_elements
