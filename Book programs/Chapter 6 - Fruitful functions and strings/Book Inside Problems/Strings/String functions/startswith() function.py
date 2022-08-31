# startswith() function
"""The startswith() function returns True if a string starts with the specified characters in the
prefix else it returns False
SYNTAX : string.startswith(prefix, start, end)
where 1) suffix - String or tuple of prefixes to be checked
      2) start (optional) - Beginning position where prefix s to be checked within the string
      3) stop (optional) - Ending position where prefix is to be checked within the string"""

string = input("Enter the string : ")
prefix_string = input("Enter the prefix string : ")

if prefix_string in string:
    print(f'The string ({string}) starts with the string ({prefix_string}) is : {string.startswith(prefix_string)}')
    print(f"The string ({string}) does starts with the string ({prefix_string})")
else:
    print(f'The string ({string}) starts with the string ({prefix_string}) is : {string.startswith(prefix_string)}')
    print(f"The string ({string}) doesn't starts with the string ({prefix_string})")
