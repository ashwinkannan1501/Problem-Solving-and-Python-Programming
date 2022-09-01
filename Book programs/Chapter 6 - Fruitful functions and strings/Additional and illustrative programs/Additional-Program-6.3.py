# Python program to search an element using binary search
# list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# search_element = int(input('Enter the search element : '))
# lowest_element = 1
# highest_element = len(list_elements)
# while lowest_element < highest_element:
#     middle_element = (lowest_element + highest_element) // 2
#     if list_elements[middle_element] == search_element:
#         print(f'The search element ({search_element}) is found inside the list ({list_elements})')
#         break
#     elif search_element < list_elements[middle_element]:
#         lowest_element = middle_element - 1
#         print(f'The search element ({search_element}) is found inside the list ({list_elements})')
#         break
#     elif search_element in list_elements:
#         highest_element = middle_element + 1
#         print(f'The search element ({search_element}) is found inside the list ({list_elements})')
#         break
#     else:
#         print(f'The search element ({search_element}) is not found inside the list ({list_elements})')
#         break

def binary_search(lists, search_element):
    lowest_element_index = 0
    highest_element_index = len(lists) - 1

    while lowest_element_index < highest_element_index:
        middle_element_index = (lowest_element_index + highest_element_index) // 2
        if search_element == lists[middle_element_index]:
            print(f"The Search element '{search_element}' is found in the list '{lists}' at position {middle_element_index}")
            break
        elif search_element < lists[middle_element_index]:
            highest_element_index = middle_element_index - 1

        elif search_element > lists[middle_element_index]:
            highest_element_index = middle_element_index + 1

    else:
        print(f"The Search Element '{search_element}' was not found in the lists '{lists}'")


list_elements = list(map(int, input("Enter the List Values Separated by commas using ony integers :- ").split(",")))
print(f"Unsorted List : {list_elements}")
list_elements.sort()
print(f"Sorted Lists : {list_elements}")
search_key = int(input("Enter the Search Key :- "))
binary_search(lists=list_elements, search_element=search_key)
