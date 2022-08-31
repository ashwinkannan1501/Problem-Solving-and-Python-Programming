# Python int() function
"""The int() function is used to returns the integer object from any number or string. It is mostly
used to converting from another data type to integer data type
SYNTAX : int(x=0, base=10)
         where x - Number or string to be converted to integer object
               base - Base of number in x. Can be 0 (code literal) or 2-36 """
float_number = float(input("Enter the float number : "))
print(f'The float number is : {float_number}')
print(f'The data type is : {type(float_number)}')

# Converting the float data type to integer data type
integer_number = int(float_number)
print(f'The integer number is : {integer_number}')
print(f'The data type is : {type(integer_number)}')
