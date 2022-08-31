# Python id() function
"""The id() function returns identity (unique integer) of an object
SYNTAX : id(object)"""
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

# Prints the unique identity of both first and second numbers using 'id()' function
print(f'The unique id of {first_number} is : {id(first_number)}')
print(f'The unique id of {second_number} is : {id(second_number)}')
