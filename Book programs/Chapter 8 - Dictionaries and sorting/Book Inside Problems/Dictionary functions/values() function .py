# values() function
"""The values() functions returns a view object that displays a list of all the values in the
dictionary. It doesn't require any parameter
SYNTAX : dictionary.values()"""

# Python program using values() function
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age, "Salary": salary}

# Printing the dictionary elements
print(f'The dictionary : {dictionary}')

# Printing only the values in the dictionary
print(f'The values in the dictionary is : {dictionary.values()}')

# Printing the data type
print(f'The data type is : {type(dictionary)}')
