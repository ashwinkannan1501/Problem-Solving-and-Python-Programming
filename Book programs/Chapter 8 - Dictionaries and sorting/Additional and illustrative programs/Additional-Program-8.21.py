# Python program for selection sort


def selection_sort(list_elements):
    for elements in range(len(list_elements)):
        smallest_element = min(list_elements[elements:])
        smallest_element_index = list_elements.index(smallest_element)
        list_elements[elements], list_elements[smallest_element_index] = list_elements[smallest_element_index], list_elements[elements]
        return list_elements


print(f'The sorted list is : {selection_sort([5, 1, 100, 65, 56, 93, 12, 0, 200, 125])}')
