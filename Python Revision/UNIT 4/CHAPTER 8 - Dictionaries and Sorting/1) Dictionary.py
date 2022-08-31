# Dictionaries

# creating a dictionary
dictionary = {"ashwin":7401421277,
              "Kannan":9444110383,
              "Amutha":9444581958}

print(dictionary)
print(type(dictionary))

# Operations on dictionary
# Accessing an element
print(dictionary["ashwin"])

# Updating
dictionary["ashwin"] = 1234567890
print(dictionary['ashwin'])

# Add / remove element
dictionary['Ritika'] = 7401421277
print(dictionary)

del dictionary['ashwin']
print(dictionary)

# Membership
print('ashwin' in dictionary)
print('Ritika' in dictionary)


# Methods on dictionary
dict2 = dictionary.copy() # copy() method
print(dict2)

print(dictionary.items()) # items() method

print(dictionary.keys()) # keys() method

print(dictionary.values()) # values() method

print(dictionary.pop("Ritika")) # pop() method
print(dictionary)

dictionary.update(dict2) # update() method
print(dictionary)

dictionary.setdefault('Ashwin',7401421277) # setdefault() method
print(dictionary)

dictionary.fromkeys(dict2) # fromkeys() method
print(dictionary)

print(len(dictionary)) # len() method

dictionary.clear() # clear() method
print(dictionary)

del dictionary
print(dictionary)


