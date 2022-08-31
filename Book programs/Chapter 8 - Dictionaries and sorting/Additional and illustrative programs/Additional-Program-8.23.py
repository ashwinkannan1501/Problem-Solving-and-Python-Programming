# Python program for merge sort


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
                j += 1 ;k += 1

            while i < len(left_half_elements):
                list_elements[k] = left_half_elements[i]
                i += 1 ; k += 1

            while j < len(right_half_elements):
                list_elements[k] = right_half_elements[j]
                j += 1 ; k += 1

    return f'The sorted list is : {list_elements}'


print(merge_sort([5, 1, 100, 65, 56, 93, 12, 0, 200, 125]))
