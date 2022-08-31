# Python script to merge two dictionaries
dictionary1 = {"1": 2, "3": 4}
dictionary2 = {"5": 6, "7": 8}
print(f'first dictionary : {dictionary1}')
print(f'Second dictionary : {dictionary2}')

merged_dictionary = dictionary1.update(dictionary2)
print(f'Merged dictionary is : {merged_dictionary}')

