# index() function
"""The index() function returns the index of a value
SYNTAX : array.index(element)"""

from array import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array("i", array_elements)
index = array_elements.index(5)
print(f'The element 5 in the index is : {index}')
