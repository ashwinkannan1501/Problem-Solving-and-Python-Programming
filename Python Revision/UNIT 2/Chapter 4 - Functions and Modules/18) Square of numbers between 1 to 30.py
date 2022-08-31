# Python function program to create and print a list where the values are square of numbers between 1 and 30

def square():
    list_values = []

    for number in range(1, 31):
        list_values.append(number ** 2)

    return list_values


print(square())
