"""Function composition - The ability of calling one function within the another function is called
function composition"""


def multiplication(addition_result, fourth_number):
    return f'The multiplication of {addition_result} x {fourth_number} is : {addition_result * fourth_number}'


def addition(first_number, second_number):
    addition_result = first_number + second_number
    return f'The addition of {first_number} + {second_number} is : {addition_result}'


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
fourth_number = int(input("Enter the fourth number : "))

print(multiplication(addition(first_number, second_number), fourth_number))  # Function composition
