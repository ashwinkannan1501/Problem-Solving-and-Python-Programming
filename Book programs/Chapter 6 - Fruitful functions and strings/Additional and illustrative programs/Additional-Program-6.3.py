# Python program to search an element using binary search
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = int(input('Enter the search element : '))
lowest_element = 1
highest_element = len(list_elements)
while lowest_element < highest_element:
    middle_element = (lowest_element + highest_element) // 2
    if list_elements[middle_element] == search_element:
        print(f'The search element ({search_element}) is found inside the list ({list_elements})')
        break
    elif search_element < list_elements[middle_element]:
        lowest_element = middle_element - 1
        print(f'The search element ({search_element}) is found inside the list ({list_elements})')
        break
    elif search_element in list_elements:
        highest_element = middle_element + 1
        print(f'The search element ({search_element}) is found inside the list ({list_elements})')
        break
    else:
        print(f'The search element ({search_element}) is not found inside the list ({list_elements})')
        break

