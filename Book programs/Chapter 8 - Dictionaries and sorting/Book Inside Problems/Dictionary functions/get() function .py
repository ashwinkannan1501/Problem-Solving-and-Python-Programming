# get() function
"""The get() function returns the value of a specified key if key is in the dictionary
SYNTAX : dictionary.get(key, value)
where 1) key - The key pair to be searched in a dictionary
      2) value (optional) - The value pair to be returned if the key is not found. The default
            value is None. whereas returns value, if the key is not found and the value is specified"""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))

dictionary = {"Name": name, "Age": age}
print(f"dictionary : {dictionary}")

print(f'Name : {dictionary.get("Name")}')
print(f'Age : {dictionary.get("Age")}')

# value is not provided
print(f'Printing "Salary" when value is not provided : {dictionary.get("Salary")}')

# Value is provided
print(f'Printing "Salary" when value is provided : {dictionary.get("Salary", salary)}')
