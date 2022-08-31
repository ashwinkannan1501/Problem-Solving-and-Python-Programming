# append() function
"""The append() function is used to add the elements at the end of an array
SYNTAX : array.append(element)"""

from array import array
array_elements = [1, 2, 3, 4, 5]
array_elements = array('i', array_elements)
array_elements.append(6)
print(f'The elements uin the array are : {array_elements}')