# Python program to convert a list into a tuple
list_elements = input("Enter the list string : ")
list_elements = list(list_elements.split(","))
print(f'The list elements are : {list_elements}')
print(f'The data type is : {type(list_elements)}')

tuple_elements = tuple(list_elements)
print(f'The tuple elements are : {tuple_elements}')
print(f'The data type is : {type(tuple_elements)}')
