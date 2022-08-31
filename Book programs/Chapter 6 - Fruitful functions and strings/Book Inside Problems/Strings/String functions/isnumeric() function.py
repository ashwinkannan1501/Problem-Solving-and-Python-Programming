# isnumeric() function
"""The isnumeric() function returns True if all the characters in a string are numeric characters
else returns False. A numeric characters has following properties:
    1) Numeric type - decimal
    2) Numeric type - digit
    3) Numeric type - Numeric
SYNTAX : string.isnumeric()"""

# Python program to check if all the characters in a string are numeric characters or not
string = input("Enter the string : ")
print(f'The characters in the string ({string}) are numeric characters : {string.isnumeric()}')
