# tuple operators

# creating a tuple
tuple_elements = tuple(input("Enter the tuple elements : ").split(","))
concatenate = tuple(input("Enter the concatenate tuple elements : ").split(","))

# Indexing
print(f'Element at position 0 in the {tuple_elements} is : {tuple_elements[0]}')
print(f'Element at position 3 in the {tuple_elements} is : {tuple_elements[2]}')

# Slicing
print(f'Accessing 1st 3 elements : {tuple_elements[:3]}')

# Concatenation
print(f'The concatenation of {tuple_elements} + {concatenate} is : {tuple_elements + concatenate}')

# Repetition
print(f'The repetition of (tuple_elements) by 3 times is : {tuple_elements * 3}')

# Membership ("in" and "not in")
print(f'{concatenate} in {tuple_elements} is : {concatenate in tuple_elements}')
print(f'{concatenate} not in {tuple_elements} is : {concatenate not in tuple_elements}')

# Comparison ("is" and "is not" (or) "==" and "!=")
print(f'Comparison of {concatenate} and {tuple_elements} using is and is not operator is : {concatenate is tuple_elements}')
print(f'Comparison of {concatenate} and {tuple_elements} using is and is not operator is : {concatenate is not tuple_elements}')
print(f'Comparison of {concatenate} and {tuple_elements} using == and != operator is : {concatenate == tuple_elements}')
print(f'Comparison of {concatenate} and {tuple_elements} using == and != operator is : {concatenate != tuple_elements}')
