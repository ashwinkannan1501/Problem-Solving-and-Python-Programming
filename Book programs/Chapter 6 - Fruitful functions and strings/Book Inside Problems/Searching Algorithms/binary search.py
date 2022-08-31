# Binary search
"""The binary search is based on 'divider and conquer' technique. Before searching, the elements in the
list or tuple must be sorted. It is first divided into equal halves. The middle element, the left
elements and the right elements"""


def binary_search(list_elements, search_element):
    lowest_element_index = 0
    highest_element_index = len(list_elements) - 1
    while lowest_element_index < highest_element_index:
        middle_element_index = (lowest_element_index + highest_element_index) // 2
        if search_element == list_elements[middle_element_index]:
            print(f'The search element ({search_element}) was found in the list ({list_elements})')
            break
        elif search_element < list_elements[middle_element_index]:
            highest_element_index = middle_element_index - 1
            print(f'The search element ({search_element}) was found in the list ({list_elements}) at index {highest_element_index}')
            break
        elif search_element > list_elements[middle_element_index]:
            lowest_element_index = middle_element_index + 1
            print(f'The search element ({search_element}) was found in the list ({list_elements}) at index {lowest_element_index}')
            break
        else:
            print(f'The search element ({search_element}) was not found in the list ({list_elements})')
            break


list_elements = [18, 2, 5, 6, 1, 0, 100, 95]
print(f'Unsorted list elements : {list_elements}')
list_elements.sort()
print(f'Sorted list elements : {list_elements}')

search_element = int(input("Enter the search element : "))

binary_search(list_elements, search_element)
