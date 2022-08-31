# Python program to check a dictionary is empty or not
dictionary = {1: 2, 3: 4}
if not dictionary.items():
    print(f'Dictionary ({dictionary}) is empty')
else:
    print(f'Dictionary ({dictionary}) is not empty')
