# Python program to work with list
list_elements = str(input("Enter the list elements : "))
list_elements = list(list_elements.split(","))

# Printing list
print(f'Printing the whole list : {list_elements}')

# Printing list with the range index slicing
print(f'Printing the list from range [2:8]')

# Positive index
print(f'Index element at position 0 : {list_elements[0]}')
print(f'Index element at position 1 : {list_elements[1]}')

# Negative Index
print(f'Index element at position -1 : {list_elements[-1]}')
print(f'Index element at position -2 : {list_elements[-2]}')

# Updating elements at specific index (Mutability)
list_elements[2] = "David bombal"
print(f'updating at index 2 : {list_elements}')

# Removing elements
list_elements.remove("ashwin")
print(list_elements)

# Inserting an element at an end
list_elements.append("Bro code")
print(f'Appending element at an last in the list : {list_elements}')
