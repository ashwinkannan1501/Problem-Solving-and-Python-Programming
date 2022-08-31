# Python program to sum all the items in the list
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sum of all the elements in the list with using built-in 'sum()' function
print(f'Sum of list elements({list_elements}) is : {sum(list_elements)}')

# Sum of all the elements in the list without using built-in 'sum()' function
total = 0
for element in list_elements:
    total += element
print(f'Sum of list elements({list_elements}) is : {total}')
