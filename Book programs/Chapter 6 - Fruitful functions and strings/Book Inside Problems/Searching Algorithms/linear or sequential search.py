# Linear search
"""The linear search is one of the searching algorithm that searches the element from sequential
order (either in ascending or in descending order)"""

# Python program to perform the linear search or sequential search


def linear_search(list_elements, searching_element):
    for search in range(len(list_elements)):
        if searching_element == list_elements[search]:
            print(f'The element ({searching_element}) was found in the list ({list_elements})')
            break
    else:
        print(f'The element ({searching_element}) was not found in the list ({list_elements})')


list_elements = [10, 20, 5, 8, 12]
searching_element = int(input("Enter the search element : "))

linear_search(list_elements, searching_element)
