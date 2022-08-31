# Python Strings
string = input("Enter the string : ")

# Prints the complete string
print(f'String : {string}')

# Prints the first character of the string
print(f'The first character of the string({string}) is : {string[0]}') # Indexing

# Prints character starting from  3rd to 5th
print(f'The character from 3rd to 5th character in the string {string} is : {string[2:6]}') # Slicing

# Prints the string starting from 3rd character
print(f'The character starting from 3rd character in the string ({string}) is : {string[2:]}')

# Prints the string two times
print(f'Twice the string ({string}) is : {string * 2}') # Multiplying the string

# Prints concatenated string
print(f'Concatenating "You are an awesome coder" to an string ({string}) is : {string + "You are an awesome person"}')
