# Python program to check if a given key is already exists in a dictionary

dictionary = {1:'Ashwin', 2:'Gowtham', 3:'Arun Kumar', 4:'Annamalai'}
print("Dictionary : ", dictionary)

key = int(input("Enter the key : "))

if(key in dictionary.keys()):
    print(f'The key "{key}" is present in the dictionary')
else:
    print(f'The key "{key}" is not present in the dictionary')
