# Insertion Sort

# sub-program
def insertion_sort(list_items, sort_order):
    if(sort_order == 'ascending'):
        for i in list_items:
            j = list_items.index(i)
            while(j > 0):
                if(list_items[j-1] > list_items[j]):
                    list_items[j-1], list_items[j] = list_items[j], list_items[j-1]
                    print(list_items)
                    j -= 1    
                else:
                    break
        print("Sorted list in ascending order : ", list_items)
        
    elif(sort_order == 'descending'):
        for i in list_items:
            j = list_items.index(i)
            while(j > 0):
                if(list_items[j-1] < list_items[j]):
                    list_items[j], list_items[j-1] = list_items[j-1], list_items[j]
                    print(list_items)
                    j -= 1    
                else:
                    print("Sorted list in descending order : ", list_items)
                    break
        print("Sorted list in descending order : ", list_items)

# Main program
lists = list(input("Enter the list items : ").split(","))  # Getting the list items from the user

list_items = []
for value in lists:
    list_items.append(int(value)) # Converting the string into integer and store it in new list

while(True):
    sort_order = input("Select the sorting order (ascending / descending) : ").lower() # Get the sorting order from the user
    if(sort_order == 'ascending' or sort_order == 'descending'): # Check if the sort_order is 'ascending' or 'descending'
        print("Unsorted List : ", list_items) # print the unsorted array
        insertion_sort(list_items, sort_order) # Pass the function call named 'insertion_sort()'
        break
    else:
        print('Please enter either "ascending"/"descending"') # Prompt the user to enter the correct order 

