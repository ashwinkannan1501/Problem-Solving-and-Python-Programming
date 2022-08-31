# Python program to find the index of an item of a tuple
tuple_elements = input("Enter the tuple elements : ")
tuple_elements = tuple(tuple_elements.split(','))
print(f'The index element is : {tuple_elements.index(tuple_elements[1])}')
print(f'The element in the index({tuple_elements.index(tuple_elements[1])}) is : '
      f'{tuple_elements[1]}')

