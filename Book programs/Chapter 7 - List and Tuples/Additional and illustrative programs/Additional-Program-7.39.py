# Python program to count the elements in a list until an element is a tuple
list_elements = [1, 2, 3, 4, 5, (6, 7), 8, 9, 10]
count = 0
for element in list_elements:
    if isinstance(element, tuple):
        break
    count += 1
    print(count)
