# pop() function
"""The pop() function is used to deletes the element at the specified index. If index is not provided,
the last element will be deleted"""

list_elements = list(input("Enter the list elements : ").split(","))

# Original list
print(f'Original list : {list_elements}')

# Popped list with the specific arguments
list_elements.pop(1)
print(f'List after popped with the specified element index : {list_elements}')

# Popped list without the specified arguments
list_elements.pop()
print(f'List after popped without the specified element : {list_elements}')
