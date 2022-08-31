"""Python program to find the sum of all the numbers sorted in a list"""
list_elements = [1, 2, 3, 4, 5, 6]

# using sum() function
print(f'The sum of {list_elements} is : {sum(list_elements)}')

# using for loop
add = 0
for elements in list_elements:
    add += elements
print(f'The sum of {list_elements} is : {add}')
