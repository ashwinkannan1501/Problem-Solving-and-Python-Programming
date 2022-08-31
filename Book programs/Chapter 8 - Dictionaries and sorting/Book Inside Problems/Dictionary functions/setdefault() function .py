# setdefault() function
"""The setdefault() function returns the value of a key (if the key is ion te dictionary). If not,
it inserts key with a value to the dictionary.
SYNTAX : dictionary.setdefault(key, default_value)
where 1) key - The key to be searched in a dictionary
      2) default_value (optional) - The value is inserted if the value is not in the dictionary.
        If value is not provided, then the default_value will be None"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age}
# Python program using setdefault() function

print(f'Dictionary before setting te default key and value pair : {dictionary}')

# setting default (key, value) pair in the dictionary
print(f'Setting the default (key, value) pair : {dictionary.setdefault("salary", salary)}')

# Printing the dictionary with the default key and value
print(f'Dictionary after setting te default key and value pair : {dictionary}')
