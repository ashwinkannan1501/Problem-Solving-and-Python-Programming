# Python tuples
tuple_elements = input("Enter the tuple elements : ")
tuple_elements = tuple(tuple_elements.split(","))

tiny_tuple_elements = input("Enter the tiny tuple elements : ")
tiny_tuple_elements = tuple(tiny_tuple_elements.split(","))

# Prints both the tuple
print(f"Tuple elements : {tuple_elements}")
print(f'Tiny tuple elements : {tiny_tuple_elements}')

# Pints he first element of the tuple
print(f'First element of the tuple {tuple_elements} is : {tuple_elements[0]}')
print(f'The first element of the tiny tuple element {tiny_tuple_elements} is {tiny_tuple_elements[0]}')

# Prints the tuple elements starting from 2nd till 3rd
print(f'The elements starting from 2nd till 3rd in the tuple {tuple_elements} is : {tuple_elements[1:3]}')
print(f'The elements starting from 2nd till 3rd in the tiny tuple {tiny_tuple_elements} is : {tiny_tuple_elements[1:3]}')

# Prints elements starting from 3rd elements
print(f'The elements starting from 3rd element in the tuple {tuple_elements} is : {tuple_elements[2:]}')
print(f'The elements starting from 3rd element in the tiny tuple {tiny_tuple_elements} is : {tiny_tuple_elements[2:]}')

# Prints the tuple two times
print(f'Multiplication of the tuple {tuple_elements} is : {tuple_elements * 2}')
print(f'Multiplication of the tiny tuple {tiny_tuple_elements} is {tiny_tuple_elements * 2}')

# Prints concatenated list
print(f'The concatenation of tuple {tuple_elements} and tiny tuple elements ({tiny_tuple_elements}) '
      f'is : {tuple_elements + tiny_tuple_elements}')
