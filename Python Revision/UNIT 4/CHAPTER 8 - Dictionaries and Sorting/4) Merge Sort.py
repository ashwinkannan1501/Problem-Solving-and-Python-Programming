# Merge Sort

# Sub-Program
def merge_sort(list_items, sort_order):
    if(sort_order == 'ascending'):
        if(len(list_items) > 1):
            middle_element = len(list_items) // 2 # Finding the middle element
            left_half = list_items[:middle_element] # Separate the left half of elements 
            right_half = list_items[middle_element:] # Separate the right half of the elements

            # Recursing the left_half and right_half unit it reaches the single element
            merge_sort(left_half, sort_order)
            merge_sort(right_half, sort_order)
            
            i = 0 # Left array index
            j = 0 # Right array index
            k = 0 # Merged array index

            while(i < len(left_half) and j < len(right_half)):
                if(left_half[i] < right_half[j]):
                    list_items[k] = left_half[i]
                    i += 1
                elif(left_half[i] > right_half[j]):
                    list_items[k] = right_half[j]
                    j += 1
                k += 1

            while (i < len(left_half)):
                list_items[k] = left_half[i]
                i += 1
                k += 1

            while(j < len(right_half)):
                list_items[k] = right_half[j]
                j += 1
                k += 1
        print(list_items)
        

    elif (sort_order == 'descending'):
        
        if(len(list_items) > 1):
            middle_element = len(list_items) // 2 # Finding the middle element
            left_half = list_items[:middle_element] # Separate the left half of elements
            right_half = list_items[middle_element:] # Separate the right half of the elements

            # Recursing the left_half and right_half unit it reaches the single element
            merge_sort(left_half, sort_order)
            merge_sort(right_half, sort_order)

            i = 0 # Left array index
            j = 0 # Right array index
            k = 0 # Merged array index

            while((i < len(left_half)) and (j < len(right_half))):
                if(left_half[i] > right_half[j]):
                    list_items[k] = left_half[i]
                    i += 1
                elif(left_half[i] < right_half[j]):
                    list_items[k] = right_half[j]
                    j += 1
                k += 1

            while (i < len(left_half)):
                list_items[k] = left_half[i]
                i += 1
                k += 1

            while(j < len(right_half)):
                list_items[k] = right_half[j]
                j += 1
                k += 1
        print(list_items)

# Main-Program
lists = list(input("Enter the list items : ").split(","))

list_items = []

for value in lists:
    list_items.append(int(value))



while(True):
    sort_order = input("Enter the sorting order ('ascending'/'descending') : ").lower()

    if(sort_order == 'ascending' or sort_order == 'descending'):
        print("Unsorted List : ", list_items)
        merge_sort(list_items, sort_order)
        break

    else:
        print('Please enter either "ascending"/"descending"')

print("Sorted List : ", list_items)
    
