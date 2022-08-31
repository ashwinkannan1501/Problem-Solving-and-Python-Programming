# Python program to find the length of the tuple
tuple_elements = input("Enter the tuple elements : ")
tuple_elements = tuple(tuple_elements.split(","))
print(f'Tuple elements are : {tuple_elements}')
print(f'The length of the tuple({tuple_elements}) is : {len(tuple_elements)}')
