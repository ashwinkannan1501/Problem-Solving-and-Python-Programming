# Python Program that takes a list and returns a new list with unique elements of the first list
duplicate_list_elements = str(input("Enter the list elements : "))
duplicate_list_elements = list(duplicate_list_elements.split(","))
list_elements = []
for elements in duplicate_list_elements:
    if elements not in list_elements:
        list_elements.append(elements)
print(list_elements)
