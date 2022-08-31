# Python program to remove duplicate element from the list
list_elements = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]
print(f'Original List : {list_elements}')

# Removing duplicate elements from the list by casting the type to set and re-casting to list
set_elements = set(list_elements)
print(f"Removing duplicate element from the list : {list(set_elements)}")

non_duplicate_list = []
for element in list_elements:
    if element not in non_duplicate_list:
        non_duplicate_list.append(element)
print(f"Removing duplicate element from the list : {non_duplicate_list}")
