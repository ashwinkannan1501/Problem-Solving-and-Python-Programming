# Program to find the maximum of a list of numbers

list_elements = [10, 5, 6, 20, 100, 95, 200, 12, 1, 0]
maximum_element = 0
for i in list_elements:
    if maximum_element < i:
        maximum_element = i

print(f'Maximum of list of numbers with using built-in "max()" function is : {max(list_elements)}')
print(f'Maximum of list of numbers without using built-in "max()" function is : {maximum_element}')
