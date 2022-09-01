# Python program to search an element using linear search
# list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# search_element = int(input("Enter the search element : "))
# for i in range(len(list_elements)):
#     if search_element in list_elements:
#         print(f'The element ({search_element}) is found inside the list ({list_elements})')
#         break
#     elif search_element not in list_elements:
#         print(f'The element ({search_element}) is not found inside the list ({list_elements})')
#         break

def sequential_search(list_elements, search_key, order):
    if order == 'a':
        for item in range(len(list_elements)):
            if search_key == list_elements[item]:
                print(f"The Element '{search_key}' was found in the list '{list_elements}' at the position {item + 1}")
                break
        else:
            print(f"The Element '{search_key}' was not found in the list '{list_elements}'")
    elif order == 'd':
        for item in range(0, len(list_elements), -1):
            if search_key == list_elements[item]:
                print(
                    f"The Element '{search_key}' was found in the list '{list_elements}' at the position {item + 1}")
                break
        else:
            print(f"The Element '{search_key}' was not found in the list '{list_elements}'")


try:
    list_elements = list(map(int, input("Enter the list values in Integers :- ").split(",")))
    search_key = int(input("Enter the Search element :- "))
    order = input("Enter the order to be searched for (Ascending / Descending) :- ").lower()[0]
except Exception as error:
    print(error)

sequential_search(order=order, search_key=search_key, list_elements=list_elements)


