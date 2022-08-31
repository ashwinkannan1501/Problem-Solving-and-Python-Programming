# Program for selection sort and insertion sort
def selection_sort(list_elements):
    for element in range(len(list_elements)):
        smallest_element = min(list_elements[element:])
        smallest_element_index = list_elements.index(smallest_element)
        (list_elements[element],
         list_elements[smallest_element_index]) = (list_elements[smallest_element_index], list_elements[element])
    print(f'Sorted List using selection sort : {list_elements}')


def insertion_sort(list_elements):
    for i in list_elements:
        j = list_elements.index(i)
        while j > 0:
            if list_elements[j - 1] > list_elements[j]:
                (list_elements[j - 1], list_elements[j]) = (list_elements[j], list_elements[j - 1])
                j -= 1
        else:
            break
    print(f'Sorted List using insertion sort : {list_elements}')


list_elements = [10, 20, 5, 1, 0, 3, 23, 19, 100, 45]
print(f'Unsorted List : {list_elements}')

selection_sort(list_elements=list_elements)
insertion_sort(list_elements=list_elements)
