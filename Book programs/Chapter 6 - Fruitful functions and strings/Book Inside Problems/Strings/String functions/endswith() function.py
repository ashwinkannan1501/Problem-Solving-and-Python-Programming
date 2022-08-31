# endswith() function
"""The endswith() function retrns true if a string ends with the specified suffix characters,
otherwise returns false
SYNTAX : string.endswith(suffix, start, end)
where 1) suffix - String or tuple of suffixes to be checked
      2) start (optional) - Beginning position where suffix s to be checked within the string
      3) stop (optional) - Ending position where suffix is to be checked within the string"""

# Program to find if a string ends with the specified suffix
string = input("Enter a string : ")
suffix_string = input("Enter a suffix string : ")
if suffix_string in string:
    print(f'The string ({string}) ends with substring ({suffix_string}) is : {string.endswith(suffix_string, 0, 10)}')
else:
    print(f'The string ({string}) ends with substring ({suffix_string}) is : {string.endswith(suffix_string, 0, 10)}')
    print(f'There is no string ({string}) ends with the substring ({suffix_string})')
