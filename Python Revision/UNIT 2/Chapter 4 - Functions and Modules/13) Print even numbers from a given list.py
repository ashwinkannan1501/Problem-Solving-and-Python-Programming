# Python program to print even numbers from a given list

def even_numbers(values):
    array = []

    for number in values:
        if int(number) % 2 == 0:
            array.append(int(number))

    return array


list_values = list(input("Enter the list values : ").split(","))

result = even_numbers(list_values)

print(f"The even numbers in {list_values} are : {result}")
