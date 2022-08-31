# List as array...
"""1) Array is a collection of similar elements. Array is not a fundamental data type like
int, string, list, tuple.
2) Needs to import the array module to use the array data type in programs.
3) Elements in the array can be accessed by index. Index starts with 0

SYNTAX : import array

SYNTAX TO CREATE AN ARRAY:
    array_name = module_name.function_name('typecode', elements)
where 1)typecode : i - integer data type
                 c - character data type
                 f - float data type
      2) elements (optional) - list (or) array elements"""

# Python program to find the sum of array elements
import array
array_elements = [1, 2, 3, 4, 5, 6]
array_elements = array.array('i', array_elements)
total_array_elements = 0
for total in array_elements:
    total_array_elements += total

# sum of array elements without using built-in "sum()" function
print(f'The sum of array elements ({array_elements}) without using built-in "sum()" function is : {total_array_elements}')

# sum of array elements with using built-in "sum()" function
print(f'The sum of array elements ({array_elements}) with using built-in "sum()" function is : {sum(array_elements)}')
