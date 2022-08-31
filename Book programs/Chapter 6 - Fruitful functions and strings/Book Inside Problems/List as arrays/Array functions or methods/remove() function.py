# remove() function
"""The remove() function is used to removes the specified element provided in the argument.
SYNTAX : array.remove(element)"""

from array import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array("i", array_elements)
array_elements.remove(5)
print(f'The elements in the array are : {array_elements}')
