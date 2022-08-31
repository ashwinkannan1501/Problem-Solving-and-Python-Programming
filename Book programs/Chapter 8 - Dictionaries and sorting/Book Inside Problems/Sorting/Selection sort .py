# Selection sort
"""Selection sort makes only one exchange for every pass through the list. In this, selection sort
looks for he largest value as it makes a pass and after completing passes, places it in the proper
location"""


def insertion_sort(list_elements):
    for elements in range(len(list_elements)):
        smallest_element = min(list_elements[elements:])
        smallest_element_index = list_elements.index(smallest_element)
        list_elements[elements], list_elements[smallest_element_index] = list_elements[smallest_element_index], list_elements[elements]

    print(f'The sorted list is : {list_elements}')


insertion_sort([5, 1, 100, 65, 56, 93, 12, 0, 200, 125])
