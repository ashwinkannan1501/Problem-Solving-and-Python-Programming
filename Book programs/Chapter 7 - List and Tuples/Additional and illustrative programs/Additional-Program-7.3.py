# Python program to multiply all the items in the list
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplication = 1
for element in list_elements:
    multiplication *= element
print(f'Multiply all the items in the list ({list_elements}) is : {multiplication}')
