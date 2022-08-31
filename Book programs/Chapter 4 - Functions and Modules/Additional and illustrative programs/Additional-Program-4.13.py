# Python program to print the even numbers from a given list
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_elements = []
for elements in list_elements:
    if elements % 2 == 0:
        even_elements.append(elements)
print(f'The even elements in the list are : {even_elements}')

