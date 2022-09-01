# Binary search
"""The binary search is based on 'divider and conquer' technique. Before searching, the elements in the
list or tuple must be sorted. It is first divided into equal halves. The middle element, the left
elements and the right elements"""


def binary_search(lists, search):
    lowest_element_index = 0
    highest_element_index = len(lists) - 1
    while lowest_element_index < highest_element_index:
        middle_element_index = (lowest_element_index + highest_element_index) // 2
        if search == lists[middle_element_index]:
            print(f'The search element ({search}) was found in the list ({lists}) at the position {lists.index(search) + 1}')
            break
        elif search < lists[middle_element_index]:
            highest_element_index = middle_element_index - 1
        elif search > lists[middle_element_index]:
            lowest_element_index = middle_element_index + 1
    else:
        print(f'The search element ({search}) was not found in the list ({lists})')


try:
    list_elements = list(map(int, input("Enter the list values in unsorted manner (Only in Integer) :- ").split(",")))
    print(f'Unsorted list elements : {list_elements}')
    list_elements.sort()
    print(f'Sorted list elements : {list_elements}')

    search_element = int(input("Enter the search element : "))

except ValueError:
    print("The Value is not defined")
except NameError:
    print("Please Provide Some Value")

else:
    binary_search(list_elements, search_element)
