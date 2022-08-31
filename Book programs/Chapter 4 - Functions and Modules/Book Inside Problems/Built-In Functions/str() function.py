# Python str() function
"""The str() function is used to returns the 'informal' or nicely printable representation
of a given object. It is mostly used for typecasting from data type to string data type
SYNTAX : str(object)"""
number = int(input("Enter a number : "))
print(f'The data type of the number {number} is : {type(number)}')
number = str(number)
print(f'The data type of the number {number} is : {type(number)}')
