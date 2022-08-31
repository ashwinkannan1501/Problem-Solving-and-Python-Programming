# reverse() function
"""The reverse() function is used to reverse the list elements.
SYNTAX : list.reverse()"""

list_elements = list(input("Enter the list elements : ").split(","))

# Before reversing the list (Original list)
print(f'Original list : {list_elements}')

# After reversing the list
list_elements.reverse()
print(f'After reversing the list : {list_elements}')
