# Remove duplicate element from the list

# One way
list_elements = [1, 2, 2, 3, 4, 4, 5, 7, 6, 6]
empty_list = []

for i in list_elements:
    if i not in empty_list:
        empty_list.append(i)

print(f'List containing duplicate elements : {list_elements}')
print(f'List without containing duplicate elements : {empty_list}')

# Another way
list_elements = set(list_elements)
list_elements = list(list_elements)
print(f'List without containing duplicate elements : {list_elements}')
