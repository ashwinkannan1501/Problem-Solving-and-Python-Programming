# insert() function
"""The insert() function is used to insert the new element at the specific position by specifying the index
SYNTAX : list.insert(index, element)"""

list_elements = list(input("Enter the list elements : ").split(","))

# Before inserting the new element
print(f'Before inserting the new element : {list_elements}')

# After inserting the new element st the specified index position
list_elements.insert(1, "reshma")
print(f'After inserting the new element : {list_elements}')
