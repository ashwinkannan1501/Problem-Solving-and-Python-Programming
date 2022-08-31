# index() function
"""The index function returns the index of the spcified element in the argument
SYNTAX : list.index(element)"""

list_elements = list(input("Enter the list elements : ").split(","))
index_finding = input("Enter the index element : ")

# Original list
print(f'Original list : {list_elements}')

# Indexing an element
print(f'The element "{index_finding}" is in the index of {list_elements.index(index_finding)}th position')
