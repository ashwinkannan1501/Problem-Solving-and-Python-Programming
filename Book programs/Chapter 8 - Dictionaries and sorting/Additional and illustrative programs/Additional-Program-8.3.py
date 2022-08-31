# Python program to concatenate following dictionaries to create a new one
dictionary1 = {1:1}
dictionary2 = {2:2}
dictionary3 = {}
for dictionary in (dictionary1, dictionary2):
    dictionary3.update(dictionary)
print(dictionary3)