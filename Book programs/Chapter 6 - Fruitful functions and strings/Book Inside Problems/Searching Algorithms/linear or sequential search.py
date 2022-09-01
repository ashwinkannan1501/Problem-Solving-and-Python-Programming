# Linear search
"""The linear search is one of the searching algorithm that searches the element from sequential
order (either in ascending or in descending order)"""

# Python program to perform the linear search or sequential search


def linear_search(lists, search_element):
    for search in lists:
        if search_element == search:
            print(f'The element ({search_element}) was found in the list ({lists})')
            break
    else:
        print(f'The element ({search_element}) was not found in the list ({lists})')


list_elements = list(map(int, input("Enter the list elements (In Integers) :- ").split(",")))
searching_element = int(input("Enter the search element : "))

linear_search(list_elements, searching_element)
