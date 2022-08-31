# Program for merge sort
def merge_sort(list_elements):
    if len(list_elements) > 1:
        middle_element = len(list_elements) // 2
        left_half_elements = list_elements[:middle_element]
        right_half_elements = list_elements[middle_element:]
        merge_sort(left_half_elements) ; merge_sort(right_half_elements)

        i = 0 ; j = 0 ; k = 0
        while (i < len(left_half_elements)) and (j < len(right_half_elements)):
            if left_half_elements[i] < right_half_elements[j]:
                list_elements[k] = left_half_elements[i]
                i += 1 ; k += 1
            else:
                list_elements[k] = right_half_elements[j]
                j += 1 ; k += 1

        while i < len(left_half_elements):
            list_elements[k] = left_half_elements[i]
            i += 1 ; k += 1

        while j < len(right_half_elements):
            list_elements[k] = right_half_elements[j]
            j += 1 ; k += 1
    return f'Sorted List Elements : {list_elements}'


list_elements = [10, 20, 5, 1, 0, 3, 23, 19, 100, 45]
print(f'Unsorted List Elements : {list_elements}')

print(merge_sort(list_elements=list_elements))
