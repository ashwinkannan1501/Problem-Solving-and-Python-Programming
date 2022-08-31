# Insertion sort
"""Although insertion sort has time complexity 'O(n2)', it works in a different way by maintaining \
a sorted sub-list in the lower position of the list"""


def insertion_sort(list_elements):
    for elements in list_elements:
        index_element = list_elements.index(elements)
        while index_element > 0:
            if list_elements[index_element - 1] > list_elements[index_element]:
                list_elements[index_element - 1], list_elements[index_element] = list_elements[index_element], list_elements[index_element - 1]
                index_element -= 1
            else:
                break
    print(f'The sorted list is : {list_elements}')


insertion_sort([5, 1, 100, 65, 56, 93, 12, 0, 200, 125])
