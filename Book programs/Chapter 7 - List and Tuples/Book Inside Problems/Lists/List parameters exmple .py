# List parameters example
# Python program to remove the first element from a list


def remove_first_element(list_elements):
    print(f'Original list elements : {list_elements}')
    list_elements.remove(list_elements[0])
    print(f'After removing 1st element from the list is : {list_elements}')


list_elements = list(input("Enter the list elements : ").split(","))
remove_first_element(list_elements)
