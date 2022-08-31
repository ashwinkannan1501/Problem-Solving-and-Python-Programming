# Python program to print a specified list after removing 0th, 4th and 5th elements
list_elements = str(input("Enter the list_elements : "))
list_elements = list(list_elements.split(","))
if len(list_elements) >= 6:
    list_elements.remove(list_elements[0])
    list_elements.remove(list_elements[4])
    list_elements.remove(list_elements[5])
    print(f'The remaining elements are : {list_elements}')
else:
    print("Enter minimum 6 elements")
