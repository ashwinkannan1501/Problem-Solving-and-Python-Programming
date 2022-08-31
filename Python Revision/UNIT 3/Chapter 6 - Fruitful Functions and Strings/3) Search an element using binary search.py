# Python program to search an element using binary search
array = list(input("Enter the list values : ").split(","))
#list_values = [55, 10, 59, 26, 86, 20, 85, 1000, 100, 200]
list_values = []
for element in array:
    list_values.append(int(element))

print("Unsorted Lists : ", list_values)
list_values.sort()
print("Sorted Lists : ", list_values)

search_element = int(input("Enter the search element : "))

lower_limit = 0
upper_limit = len(list_values) - 1

while(lower_limit <= upper_limit):
    middle_element = (lower_limit + upper_limit) // 2

    if(search_element == list_values[middle_element]):
        print(f"The element {search_element} was found in the list at position {middle_element + 1}")
        break
    elif(search_element < list_values[middle_element]):
        upper_limit = middle_element - 1
    elif(search_element > list_values[middle_element]):
        lower_limit = middle_element + 1
else:
    print(f"The element {search_element} was not found in the list")
