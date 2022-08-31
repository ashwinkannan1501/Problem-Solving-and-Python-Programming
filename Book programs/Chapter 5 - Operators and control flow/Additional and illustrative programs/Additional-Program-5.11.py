"""Python program to convert decimal number into binary, octal and hexadecimal number system"""
decimal_number = int(input("Enter a decimal number : "))

# Using built-in 'bin()' function to convert into binary number
print(f'Conversion of decimal number ({decimal_number}) into binary number is : {bin(decimal_number)}')

# Using built-in 'oct()' function to convert into octal number
print(f'The conversion of decimal number ({decimal_number}) into octal number is : {oct(decimal_number)}')

# Using built-in 'hex()' function to convert into hexadecimal number
print(f'The conversion of decimal number ({decimal_number}) into hexadecimal number is : {hex(decimal_number)}')
