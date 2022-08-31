# count() function
"""The count() function is used to count the number of particular element in an array.
SYNTAX : array.count(element)"""

from array import array
array_elements = [1, 2, 3, 4, 5, 5, 6]
array_elements = array("i", array_elements)
count = array_elements.count(5)
print(f'The number of 5 in the array is : {count}')
