# Python program to get the largest number from the list
list_elements = [9, 5, 8, 7, 6, 10, 20, 50, 33, 65, 1, 0]

# Finding largest number from the list with using built-in 'max()' function
print(f"Largest element in the list ({list_elements}) is : {max(list_elements)}")

# Finding largest number from the list by sorting them first and printing last element
list_elements.sort()
print(f'Largest element in the list ({list_elements}) is : {list_elements[-1]}')

# Finding largest number from the list without using built-in 'max()' function
maximum = list_elements[0]
for element in  list_elements:
    if element > maximum:
        maximum = element
print(f'Largest element in the list ({list_elements}) is : {maximum}')
