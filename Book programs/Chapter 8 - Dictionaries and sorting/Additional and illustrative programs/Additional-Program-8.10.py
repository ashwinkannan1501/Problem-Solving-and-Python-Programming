# Python program to iterate over dictionaries using for loops
dictionary = {"NAME ": "Ashwin",
              "ROLL:NO ": "2019ECCS365",
              "REG:NO ": "211419104026",
              "SUBJECT ": "PYTHON"}
for (key, value) in dictionary.items():
    print(f'{key} : {value}')
