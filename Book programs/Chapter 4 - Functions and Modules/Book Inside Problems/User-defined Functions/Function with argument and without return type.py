# Example for Function with argument and without return type


def arithmetic_operations(first_number, second_number):

    print(f'The addition of {first_number} + {second_number} is : {first_number + second_number}')

    print(f'The subtraction of {first_number} - {second_number} is : {first_number - second_number}')

    print(f'The multiplication of {first_number} x {second_number} is : {first_number * second_number}')

    print(f'The division of {first_number} / {second_number} is : {first_number / second_number}')


first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
arithmetic_operations(first_number, second_number)
