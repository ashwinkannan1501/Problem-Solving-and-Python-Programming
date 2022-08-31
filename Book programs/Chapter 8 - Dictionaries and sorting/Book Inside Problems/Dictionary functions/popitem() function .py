# popitem() function
"""The popitem() function returns and removes the last element (key, value) pair from the
dictionary. It doesn't take any parameters
SYNTAX : dictionary.popitem()"""

# Python program using popitem() function
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age, "Salary": salary}

# Printing the dictionary before popped
print(f'Dictionary before popped : {dictionary}')

# Popped item
print(f'Popped element : {dictionary.popitem()}')

# Printing the dictionary after popped
print(f'Dictionary after popped : {dictionary}')
