# Python program to check whether a number is in the range of 1 to 10
try:

    def range_check(integer):
        if integer in range(1, 11):
            return f'The number "{integer}" is in range between 1 to 10'
        else:
            return f'The number "{integer}" is not in range between 1 to 10'


    number = int(input("Enter a number : "))

    print(range_check(number))

except ValueError:
    print("Please enter only the numbers")
