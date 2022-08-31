# Python Program to concatenate all elements in a list into a string and return it
def concatenate(list_elements):
    result = ''
    for number in list_elements:
        result += number
    return result


list_elements = str(input("Enter the list elements : "))
list_elements = list(list_elements.split(","))
print(f'The concatenated list elements are {concatenate(list_elements)}')
