# Python program to search an element using linear search

list_values = list(input("Enter the list values : ").split(","))
search_element = int(input("Enter the search element : "))

for index in range(len(list_values)):
    if(search_element == int(list_values[index])):
        print(f"The element {search_element} was found in the list at position {index + 1}")
        break

else:
    print(f"The element {search_element} was not found in the list")
