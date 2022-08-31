# partition() function
"""The partition() function is used to split the given string using the specified separator and
return a tuple with three arguments
SYNTAX : string.partition(separator)
where 1) separator - used to separate the string with specified character in-between them"""

# Python program using partition() function for splitting a string
string = input("Enter a string : ")
separator = "-"
print(f'Separate {separator} in {string} using partition() function : {string.partition(separator)}')
