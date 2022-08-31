# array() function
"""The array() function is used to create an array with data type and the list value specified
in its arguments.
SYNTAX : array.array(data_type, value_list)
where 1) data_type - type of the data
      2) value_list - list values"""

from array import array
array_elements = [1, 2, 3, 4, 5]
array_elements = array('i', array_elements)
print(f'The elements in the array are : {array_elements}')
