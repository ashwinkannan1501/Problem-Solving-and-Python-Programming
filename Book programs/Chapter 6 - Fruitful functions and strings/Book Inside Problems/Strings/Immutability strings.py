# Immutability - Python strings are immutable (i.e) not changeable after initialization
"""Python program to show that string object doesn't support item assignment, item deletion and whole string deletion"""

string = input("Enter the string : ")

# String doesn't support item assignment after initialization
string[0] = "l"
print(string)

# String doesn't support item deletion after initialization
del string[0]
print(string)

# String doesn't support whole string deletion after initialization
del string
print(string)
