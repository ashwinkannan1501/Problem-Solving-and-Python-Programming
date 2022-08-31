# Dictionary operations

# Creating a dictionary
dictionary = {1: "one", 2: "two", 3: "three"}

# Accessing an element
print(f'Accessing the 1st element : {dictionary[1]}')
print(f'Accessing the 2nd element : {dictionary[2]}')

# Update
print(f'Old dictionary is : {dictionary}')
dictionary[1] = "ONE"
print(f'Updated dictionary is : {dictionary}')

# Add element
dictionary[4] = "four"
print(f'New dictionary : {dictionary}')

# Membership operator ("in" and "not in")
print(f'"One" in dictionary is : {1 in dictionary}')
print(f'"Five" not in dictionary is : {5 not in dictionary}')
