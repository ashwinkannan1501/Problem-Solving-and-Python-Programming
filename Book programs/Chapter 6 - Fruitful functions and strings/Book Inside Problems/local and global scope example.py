"""local scope - A variable inside a function is local to that sub-function is called local scope
and its visible only to that particular sub-function
global scope - A variable defined in a main body of a loop (main function) is called a global scope
and is visible throughout the life"""

# Python program to demonstrate local and global scope


def addition(first_number, second_number):
    result = first_number + second_number  # local scope
    print(f'The addition of {first_number} + {second_number} is : {result}')


first_number = int(input("Enter the first number : "))  # global scope
second_number = int(input("Enter the second number : "))  # global scope
addition(first_number, second_number)
