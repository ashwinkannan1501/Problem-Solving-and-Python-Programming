# items() function
"""The items() function returns a view object that displays a list of dictionary's (key, value)
tuple pairs. It doesn't take any parameter
SYNTAX : dictionary.items()"""

# Python programs using items() function
first_person_name = input("Enter your name : ")
first_person_Phone_number = int(input("Enter your phone number : "))

second_person_name = input("Enter your name : ")
second_person_phone_number = int(input("Enter your phone number : "))

dictionary = {first_person_name: first_person_Phone_number, second_person_name: second_person_phone_number}
print(f'The Dictionary is : {dictionary}')

# Printing items (key, value) in a dictionary
print(f'Items (key, value) in a dictionary : {dictionary.items()}')

# Printing the data type
print(f'The data type is : {type(dictionary.items())}')
