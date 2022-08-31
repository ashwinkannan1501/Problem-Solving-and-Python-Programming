# Example for Function with argument and with return type


def arithmetic_operations(first_number, second_number):
    
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    division = first_number / second_number

    return f'The addition of {first_number} + {second_number} is : {addition} \n' \
           f'The subtraction of {first_number} - {second_number} is : {subtraction} \n' \
           f'The multiplication of {first_number} x {second_number} is : {multiplication} \n' \
           f'The division of {first_number} / {second_number} is : {division}'


first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))

print(arithmetic_operations(first_number, second_number))
