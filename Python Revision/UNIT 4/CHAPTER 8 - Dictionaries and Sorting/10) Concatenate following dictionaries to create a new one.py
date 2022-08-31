# Python program to concatenate the following dictionaries to create a new one
dictionary1 = {1:10, 2:20}
dictionary2 = {3:30, 4:40}
dictionary3 = {}

for items in (dictionary1, dictionary2):
    dictionary3.update(items)

print("Dictionary 1 : ", dictionary1)
print("Dictionary 2 : ", dictionary2)
print("Dictionary 3 : ", dictionary3)
