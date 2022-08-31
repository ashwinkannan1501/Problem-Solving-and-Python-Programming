# Selection sort

# Sub-Program
def selection_sort(list_items, sort_order):

    if(sort_order == 'ascending'): # Checking if the sort order is 'ascending'
        print('Sort numbers in ascending order')

        for index in range(len(list_items)): # Iterating over n times until all elements are sorted in ascending order
            smallest_value = min(list_items[index:]) # Find the minimum value
            smallest_index = list_items.index(smallest_value) # Find the index of that minimum value

            list_items[index], list_items[smallest_index] = list_items[smallest_index], list_items[index]    # Replace the first value of unsorted array with the minimum value
            
            print(list_items) # print the list items

        print("Sorted List in ascending order : ", list_items) # Print the sorted array
            
    elif(sort_order == 'descending'): # Checking if the sort order is 'descending'
        print('Sort numbers in descending order')
        
        for index in range(len(list_items)): # Iterating over n times until all elements are sorted in descending order
            largest_value = max(list_items[index:]) # Find the maximum value
            largest_index = list_items.index(largest_value) # Find the index of that maximum value

            list_items[largest_index], list_items[index] = list_items[index], list_items[largest_index]   # Replace the last value of unsorted array with the maximum value

            print(list_items) # Print the list items

        print("Sorted List in descending order : ", list_items) # print the sorted array

    
# Main Program
lists = list(input("Enter the list items : ").split(",")) # Getting the list items from the user

list_items = []

for value in lists:
    list_items.append(int(value)) # Converting the string into integer and store it in new list

while(True):
    sort_order = input("Select the sorting order (ascending / descending) : ").lower() # Get the sorting order from the user
    if(sort_order == 'ascending' or sort_order == 'descending'): # Check if the sort_order is 'ascending' or 'descending'
        print("Unsorted List : ", list_items) # print the unsorted array
        selection_sort(list_items, sort_order) # Pass the function call named 'selection_sort()'
        break
    else:
        print('Please enter either "ascending"/"descending"') # Prompt the user to enter the correct order 




