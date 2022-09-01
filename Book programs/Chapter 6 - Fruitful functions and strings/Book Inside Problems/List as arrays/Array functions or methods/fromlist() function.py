# fromlist() function
"""The fromlist() function is used to concatenate a list elements into array of elements
SYNTAX : array.fromlist(list_elements)"""

from array import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array("i", array_elements)
array_elements.fromlist([100, 200])
print(f'The elements in the array are : {array_elements}')
