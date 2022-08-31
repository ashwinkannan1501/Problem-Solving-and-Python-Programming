# Python program to remove an item from an tuple
tuple_elements = str(input("Enter the tuple elements : "))
tuple_elements = tuple(tuple_elements.split(","))
print(f'The tuple elements are : {tuple_elements}')

list_elements = list(tuple_elements)
#print(f'The removed element is : {tuple(list_elements.pop(2))}')
list_elements.remove(tuple_elements[2])
print(f'The tuple element after remove an item is : {tuple(list_elements)}')
