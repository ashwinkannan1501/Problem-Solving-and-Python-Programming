# Python program to access element from a list
list_elements = input("Enter the list elements : ")
list_elements = list_elements.split(",")

# printing the whole list
print(f'List elements : {list_elements}')

# Accessing individual element from the list by positive indexing
print(list_elements[0]) ; print(list_elements[1])

# Accessing individual element from the list by negative indexing
print(list_elements[-1]) ; print(list_elements[-2])

# Extending multiple elements in the list at the same time
print(f'Extended elements : {list_elements.extend("Manny ortiz, V2K Photography")}')
print(f'Printing an entire list after extending : {list_elements}')

# Appending an element in the list
print(f'Appended element : {list_elements.append("Jared Polin")}')
print(f'Printing an entire list after appending : {list_elements}')

# Inserting an element in the list at the specific position
print(f'Inserted elements at the 4th index : {list_elements.insert(4, "Just Karthik")}')
print(f'Printing an entire list after inserting an element : {list_elements}')

# Deleting an element in the list at the specific position
print(f'Deleted element in the list at the position 4 : {list_elements.remove("Just Karthik")}')
print(f'Printing an entire list after deleting an element : {list_elements}')

# Removing only the last element from the list
print(f'Removing only the last elements from the list : {list_elements.pop()}')
print(f'Printing an entire list after removing an element from the last : {list_elements}')

# Delete the whole element in the list
print(f'Deleting an entire list : {list_elements.remove(list_elements)}')
print(f'Printing an entire list after removing an element an entire list : {list_elements}')
