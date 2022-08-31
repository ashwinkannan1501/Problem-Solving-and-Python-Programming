# Python program to clone or copy a list
list_elements = input("Enter the list elements : ")
list_elements = list(list_elements.split(","))
print(f'Original list : {list_elements}')

# Copy a list with using list's built-in 'copy()' function
print(f'Clone list : {list_elements.copy()}')

# Copy a list without using list's built-in 'copy()' function
copy_list = []
for element in list_elements:
    if element not in copy_list:
        copy_list.append(element)
print(f'Copied list : {copy_list}')
