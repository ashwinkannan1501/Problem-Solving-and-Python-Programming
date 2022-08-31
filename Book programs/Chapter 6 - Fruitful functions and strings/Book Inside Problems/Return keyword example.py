# Return keyword example
"""The 'return' keyword is used to returns the value from the sub-program to the main program"""
# Python program to add two numbers using return statement


def addition(first_number, second_number):
    return f'The addition of {first_number} + {second_number} is : {first_number + second_number}'


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

print(addition(first_number=first_number, second_number=second_number))

