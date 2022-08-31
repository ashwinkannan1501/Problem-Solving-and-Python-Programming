# update() function
"""The update() function will adds the new dictionary with the existing dictionary
SYNTAX : dictionary.update(others)
where 1) others (optional) - It will update the dictionary"""

# Python program using update() function
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age}

# Printing the dictionary before updating
print(f'The dictionary before updating is : {dictionary}')

# Updating the dictionary
dictionary.update({"Salary": salary})

# Printing the dictionary after updating
print(f'The dictionary after updating is : {dictionary}')
