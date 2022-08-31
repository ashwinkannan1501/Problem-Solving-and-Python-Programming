# Program to ind the first and second largest element in the list

list_elements = [2, 9, 4, 6, 1, 0, 100, 56, 95, 45]
print(f'Unsorted list elements : {list_elements}')
list_elements.sort()
print(f'Sorted List elements : {list_elements}')
print(f'The largest element in the list is : {max(list_elements)}')
print(f'The second largest element in the list is : {list_elements[-2]}')
