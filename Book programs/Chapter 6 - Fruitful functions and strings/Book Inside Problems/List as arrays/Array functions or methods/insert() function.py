# insert() function
"""The insert() function is used to add the value at the specified position (index) in the rgument
SYNTAX : array.insert(index, element)"""

from array import array
array_elements = [1, 2, 3, 4, 5]
array_elements = array('i', array_elements)
array_elements.insert(2, 6)
print(f'The elements in the array are : {array_elements}')
