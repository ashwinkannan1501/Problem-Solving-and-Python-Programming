# Program for linear and binary search


def linear_search(list_elements, searching_element):
    for element in range(len(list_elements)):
        if searching_element == list_elements[element]:
            print(f'The element ({searching_element}) is found inside the list')
            break
    else:
        print(f'The element ({searching_element}) is not found inside the list')


def binary_search(list_elements, searching_element):
    left_elements_index = 0 ; right_elements_index = len(list_elements)-1
    middle_element_index = len(list_elements) // 2
    while left_elements_index < right_elements_index:
        if searching_element == list_elements[middle_element_index]:
            print(f'The element ({searching_element}) was found inside the list')
            break
        elif searching_element < list_elements[middle_element_index]:
            right_elements_index = middle_element_index - 1
            print(f'The element ({searching_element}) was found inside the list')
            break

        elif searching_element > list_elements[middle_element_index]:
            left_elements_index = middle_element_index + 1
            print(f'The element ({searching_element}) was found inside the list')
            break
    else:
        print(f'The element ({searching_element}) was not found inside the list')


list_elements = [10, 20, 5, 1, 0, 3, 23, 19, 100, 45]
print(f'Unordered List : {list_elements}')
list_elements.sort()
print(f'Ordered List : {list_elements}')

searching_element = int(input("Enter the searching element : "))

linear_search(list_elements=list_elements, searching_element=searching_element)
binary_search(list_elements=list_elements, searching_element=searching_element)
