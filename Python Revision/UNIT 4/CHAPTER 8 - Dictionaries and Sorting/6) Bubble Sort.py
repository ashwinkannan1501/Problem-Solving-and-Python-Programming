# Bubble Sort

#Sub-Program
def bubble_sort(list_items, sort_order):

    if(sort_order == 'ascending'):
        for i in range(len(list_items)): # Traverse through all array elements
            for j in range(len(list_items)-i-1): # Last i elements are already sorted
                # traverse the array from 0 to len(list_items)-i-1
                if(list_items[j] > list_items[j+1]): # Swap if the element found is greater than the next element
                    
                    list_items[j], list_items[j + 1] = list_items[j + 1], list_items[j]
                    print(list_items)
            print(list_items)

    elif(sort_order == 'descending'):
        for i in range(len(list_items)):
            for j in range(len(list_items)-i-1):
                if(list_items[j] < list_items[j + 1]): # Swap if the element found is lesser than the next element
                    
                    list_items[j], list_items[j + 1] = list_items[j + 1], list_items[j]
                    print(list_items)
            print(list_items)
                    
                
# Main Program
lists = list(input("Enter the list items : ").split(","))
list_items = []
for value in lists:
    list_items.append(int(value))

while(True):
    sort_order = input("Enter the sorting order ('ascending'/'descending') : ").lower()
    if(sort_order == 'ascending' or sort_order == 'descending'):
        print("Unsorted list : ", list_items)
        bubble_sort(list_items, sort_order)
        print('Sorted list : ', list_items)
        break
    else:
        print("Please enter either 'ascending'/'descending'")
