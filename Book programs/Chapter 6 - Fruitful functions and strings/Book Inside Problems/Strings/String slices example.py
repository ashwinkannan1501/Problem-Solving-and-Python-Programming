"""String slice - A segment of string is called as a string slice. The 'slice' syntax is used to refer
the sub parts of sequences like strings and lists
SYNTAX : sub_string = original_string[start:stop:end]"""
# Python program to demonstrate string slicing\
string = input("Enter the string : ")

# Prints the full string through slicing
print(f'String : {string[:]}')

# Prints the string range from 2 to 5
print(f'String range slice from 2 to 5 : {string[2:6]}')

# Prints the string range from 2 to 8 and step to 2
print(f'String range slice from 2 to 8 and step to 2 : {string[2:9:2]}')

# Prints the string in descending order
print(f'String in descending order : {string[::-1]}')
