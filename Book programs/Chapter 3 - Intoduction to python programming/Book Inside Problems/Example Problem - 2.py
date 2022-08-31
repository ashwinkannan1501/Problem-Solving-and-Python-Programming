# Python lists
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))

tiny_list_elements = input("Enter the list elements : ")
tiny_list_elements = list(tiny_list_elements.split(","))

# Prints the complete list
print(f'The list elements are : {list_elements}')
print(f'The list elements are : {tiny_list_elements}')

# Prints the first letters of the list
print(f'The first letter of the list ({list_elements}) is : {list_elements[0]}')
print(f'The first letter of the list ({tiny_list_elements}) is : {tiny_list_elements[0]}')

# Prints the element starting from 2nd till 3rd
print(f'The element starting from 2nd till 3rd in the list ({list_elements}) is : {list_elements[1:3]}')
print(f'The element starting from 2nd till 3rd in the list ({tiny_list_elements}) is : {tiny_list_elements[1:3]}')

# Prints the elements from 3rd elements
print(f'The starting from 3rd element in the list ({list_elements}) is : {list_elements[2:]}')
print(f'The starting from 3rd element in the list ({tiny_list_elements}) is : {tiny_list_elements[2:]}')

# Prints the list two times
print(f'The multiplication of list ({list_elements}) is : {list_elements * 2}')
print(f'The multiplication of list ({tiny_list_elements}) is : {tiny_list_elements * 2}')

# Prints the concatenated list
print(f'The concatenated list is : {list_elements + tiny_list_elements}')
