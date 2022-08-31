# Python program to remove duplicates from the dictionary
duplicate_dictionary = {1: 2, 3: 4, 1: 2}
original_dictionary = {}
for (key, value) in duplicate_dictionary.items():
    if value not in duplicate_dictionary:
        original_dictionary[key] = value
print(original_dictionary)
