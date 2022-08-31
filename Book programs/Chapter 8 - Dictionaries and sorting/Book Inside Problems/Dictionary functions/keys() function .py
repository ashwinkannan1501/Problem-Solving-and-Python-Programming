# keys() function
"""The keys() function returns a view object that displays a list of all the keys in the dictionary.
It doesn't take any parameters
SYNTAX : dictionary.keys()"""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age, "Salary": salary}

# Printing the dictionary
print(f'The dictionary is : {dictionary}')

# Printing only the keys in the dictionary
print(f'The keys in the dictionary is : {dictionary.keys()}')
