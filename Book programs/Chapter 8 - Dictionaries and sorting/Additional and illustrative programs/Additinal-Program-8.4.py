# Python program to check if a given key already exists in a dictionary
dictionary = {1: 2, 3: 4, 5: 6}
key = int(input('Enter a key : '))
if key in dictionary.keys():
    print(f"The key({key}) is already exists in a dictionary")
else:
    print(f'The key({key}) is not exists in a dictionary ')
