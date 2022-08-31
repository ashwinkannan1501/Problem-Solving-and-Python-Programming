# Python program to circulate n variables in a list

def circulate(value):
    print(value)

    for index in range(1, (len(value) + 1)):
        print(value[index:] + value[: index])


values = list(input("Enter the list values : ").split(","))

circulate(values)
