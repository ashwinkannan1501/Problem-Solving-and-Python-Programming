# Python program to remove duplicates from a dictionary

dictionary = {1:'Ashwin', 2:'Vignesh', 3:'Ashwin', 4:'Varatharaj'}

new_dictionary = {}

for key, value in dictionary.items():
    if(value not in new_dictionary.values()):
        new_dictionary[key] = value

print("Old Dictionary : ", dictionary)
print("New Dictionary : ", new_dictionary)
