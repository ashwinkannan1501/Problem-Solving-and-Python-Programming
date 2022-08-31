# Python dictionary
dictionary = {}
for key in range(1, 6):
    for value in range(key):
        dictionary[key] = value + 1

# Prints the complete dictionary
print(f'The dictionary is : {dictionary}')

# Prints the data type
print(f'Type of the data is : {type(dictionary)}')

# Prints the value of "1" key
print(f'The value of key 1 is : {dictionary[1]}')

# Prints all the keys in the dictionary
print(f'Dictionary keys : {dictionary.keys()}')

# Prints all the values in the dictionary
print(f'Dictionary values : {dictionary.values()}')
