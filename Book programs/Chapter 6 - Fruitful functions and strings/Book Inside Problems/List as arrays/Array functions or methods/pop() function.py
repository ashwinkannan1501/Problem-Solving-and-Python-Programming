# pop() function
"""The pop() function is used to remove the element by specifying the index. Otherwise, removes last element.
SYNTAX : array.pop(index)"""

from array import array
array_element = [1, 2, 3, 4, 5, 6]
array_element = array("i", array_element)
array_element.pop(2)
print(f'The elements in the array are : {array_element}')
