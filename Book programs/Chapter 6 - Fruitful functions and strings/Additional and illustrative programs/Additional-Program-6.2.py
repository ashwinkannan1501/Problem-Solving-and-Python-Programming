# Python program to search an element using linear search
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = int(input("Enter the search element : "))
for i in range(len(list_elements)):
    if search_element in list_elements:
        print(f'The element ({search_element}) is found inside the list ({list_elements})')
        break
    elif search_element not in list_elements:
        print(f'The element ({search_element}) is not found inside the list ({list_elements})')
        break


