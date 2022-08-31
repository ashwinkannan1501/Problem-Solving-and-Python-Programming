# Quick Sort

def quick_sort(list_items, left, right):
    if(left < right):
        partition_position = partition(list_items, left, right)
        quick_sort(list_items, left, partition_position - 1)
        quick_sort(list_items, partition_position + 1, right)

def partition(list_items, left, right):
    i = left
    j = right - 1
    pivot = list_items[right]

    while(i < j):
        while(i < right and list_items[i] <= pivot):
            i += 1
        while(j < left and list_items[j] >= pivot):
            j -= 1
        if(i < j):
            list_items[i], list_items[j] = list_items[j], list_items[i]

    if(list_items[i] > pivot):
        list_items[i], list_items[right] = list_items[right], list_items[i]

    return i

lists = list(input("Enter the list items : ").split(","))
list_items = []
for value in lists:
    list_items.append(int(value))

print("Unsorted list : ", list_items)
quick_sort(list_items, 0, len(list_items) - 1)
print("Sorted list : ", list_items)
