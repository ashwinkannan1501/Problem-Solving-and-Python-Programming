# Python program to sum all numbers in a list
try:
    def sum_values(values):
        total = 0

        for number in values:
            total += int(number)

        return total


    list_values = list(input("Enter the list values : ").split(","))

    result = sum_values(list_values)

    print(f"The Sum of list {list_values} is : {result}")

except ValueError:
    print("You should enter only numbers (i.e) Integers")
