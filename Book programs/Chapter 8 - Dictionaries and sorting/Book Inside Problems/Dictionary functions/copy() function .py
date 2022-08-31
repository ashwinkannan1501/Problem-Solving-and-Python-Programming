# copy() function
"""The copy() function returns a shallow copy of a dictionary
SYNTAX : dictionary.copy()"""

# Creating a dictionary
dictionary = {1: "one", 2: "two", 3: "three"}

# Copying the dictionary - This function is used to put the copied elements in a dictionary in a separate memory \
# locations
dictionary_copy = dictionary.copy()

print(f'Original dictionary : {dictionary}')
print(f'Copied dictionary : {dictionary_copy}')

# Adding the new element to the original dictionary
dictionary[4] = "Four"

# Printing both the dictionaries after updating the original dictionary
print(f'Original dictionary : {dictionary}')
print(f'Copied dictionary : {dictionary_copy}')
