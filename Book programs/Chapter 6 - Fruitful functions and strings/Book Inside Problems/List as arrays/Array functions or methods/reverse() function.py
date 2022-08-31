# reverse() function
"""The reverse() function is used to reverse the elements in the array
SYNTAX : array.reverse()"""

from array import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array("i", array_elements)
array_elements.reverse()
print(f'The reversed elements in the array are : {array_elements}')
