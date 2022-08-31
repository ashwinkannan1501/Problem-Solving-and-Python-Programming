# python set() function
"""The set() function is used to constructs and returns a python set from the given iterable
SYNTAX : set([iterable])
         where iterable (optional) - a sequence (string, tuple, list, etc) or a collection (set, dictionary, etc) or
                an iterator object to be converted into a set"""

# Empty set
print(f'Empty set - {set({})}')

# Type cast from tuple to set
tuple_elements = input("Enter the tuple elements : ")
tuple_elements = tuple(tuple_elements.split(","))
print(f'The type cast from tuple ({tuple_elements}) to set is : {set(tuple_elements)}')

# Type cast from list to set
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))
print(f'The type cast from list ({list_elements}) to set is : {set(list_elements)}')

# from range to set
range_items = range(1, 11)
print(f'Converting range to set is : {set(range_items)}')
