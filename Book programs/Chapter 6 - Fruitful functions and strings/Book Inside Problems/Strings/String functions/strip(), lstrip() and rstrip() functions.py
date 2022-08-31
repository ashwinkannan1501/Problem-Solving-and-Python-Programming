# strip() function
"""The strip() function is used to remove the unwanted whitespace from the string.
SYNTAX : string.strip(chars)
where 1) chars (optional) - a string specifying the set of characters to be removed. If the characters
        are not provided, all the leading and trailing whitespaces are removed from the string"""

# lstrip() function
"""The lstrip() function returns a copy of a string with the leading characters are removed
SYNTAX : string.lstrip(chars)
where 1) chars (optional) - a string specifying the set of characters to be removed. If the characters 
        are not provided, all the leading whitespaces are removed from the string"""

# rstrip() function
"""The rstrip() function returns a copy of a string with the trailing characters are removed
SYNTAX : string.rstrip(chars)
where 1) chars (optional) - a string specifying the set of characters to be removed. If the characters 
        are not provided, all the trailing whitespaces are removed from the string"""

string = input("Enter a string : ")
print(f'Remove unwanted leading and trailing string characters ({string}) using strip() function : {string.strip("q")}')
print(f'Remove unwanted leading string characters ({string}) using lstrip() function : {string.lstrip("q")}')
print(f'Remove unwanted trialing string characters ({string}) using rstrip() function : {string.rstrip("q")}')
