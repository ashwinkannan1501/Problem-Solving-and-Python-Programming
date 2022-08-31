# Python program that takes a list and returns a new list with unique elements of the first list

def unique_elements(values):
    new_list = []

    for number in values:
        if number not in new_list:
            new_list.append(number)

    return new_list


list_values = list(input("Enter the list values : ").split(","))

result = unique_elements(list_values)

print("The unique set of list values is : ", result)
