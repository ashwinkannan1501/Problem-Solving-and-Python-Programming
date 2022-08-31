# casefold() function
"""The casefold() function removes all the case distinctions present in a string. It is used for
caseless matching. It doesn't take any parameters. Basically, the 'casefold()' function converts the
uppercase letters to lowercase letters
SYNTAX : string.casefold()"""

string = input("Enter a string : ")
print(f'Before casefold (UPPERCASE LETTERS) : {string}')
print(f'After casefold (lowercase letters) : {string.casefold()}')
