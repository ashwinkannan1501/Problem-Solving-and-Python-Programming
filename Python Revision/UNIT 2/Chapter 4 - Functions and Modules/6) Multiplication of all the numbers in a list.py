# Python program to multiply all the numbers in a list
try:
    def multiply_list(values):
        multiply = 1

        for number in values:
            multiply *= int(number)

        return multiply


    list_values = list(input("Enter the list values : ").split(","))

    result = multiply_list(list_values)

    print(f'The multiplication of {list_values} is : {result}')

except ValueError:
    print("You should enter only numbers (i.e) Integers")
