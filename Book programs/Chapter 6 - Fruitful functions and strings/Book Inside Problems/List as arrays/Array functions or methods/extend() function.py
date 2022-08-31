# extend() function
"""The extend() function is used to extends the one array of elements with the another arrauy of elements
SYNTAX : array.extend(array_elements)"""

from array import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array("i", array_elements)
array_elements.extend([100, 200])
print(f'The extended elements in the array are : {array_elements}')
