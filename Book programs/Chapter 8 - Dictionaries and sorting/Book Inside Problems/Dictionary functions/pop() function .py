# pop() function
"""The pop() function removes and returns an element from an dictionary with the given key in the argument.
SYNTAX : dictionary.pop(key, default)
where 1) key - The key which is to be removal
      2) default (optional) - value to be returned when the key is not in te dictionary. If value
        is not provided, returns an KeyError exception"""

# Python program using pop() function
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age, "Salary": salary}

# Printing the dictionary before popped
print(f'Dictionary before popped : {dictionary}')

# Popped element
print(f'Popped element : {dictionary.pop("Age", age)}')

# Printing the dictionary after popped
print(f'Dictionary after popped : {dictionary}')
