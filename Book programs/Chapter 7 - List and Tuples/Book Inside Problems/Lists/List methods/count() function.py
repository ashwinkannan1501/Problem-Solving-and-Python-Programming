# count() function
"""The count() function is used to counts the number of times the eleemnts occurs in the list
SYNTAX : list.count(element)"""

list_elements = list(input("Enter the list elements : ").split(","))
searching_element = input("Enter the searching element : ")

# List elements
print(f'Original list : {list_elements}')

# Number of times the element occurs in the list
print(f'The string ({searching_element}) occurs {list_elements.count(searching_element)} times in the list ')
