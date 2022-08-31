"""Parameters and arguments - Parameters (also known as arguments) are input to the functions.
Parameters are used in function definition and arguments are used in function call"""
# Python program to find the addition of two numbers by passing parameters


def addition(first_number, second_number):  # parameters
    return f'The addition of {first_number} + {second_number} is : {first_number + second_number}'


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
print(addition(first_number=first_number, second_number=second_number))  # arguments
