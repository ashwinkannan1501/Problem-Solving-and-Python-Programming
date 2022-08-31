# Python program to sort (ascending and descending) a dictionary by value
# Import the 'operator' module
import operator
dictionary = {1:3, 2:5, 10:6, 0:0}
print(f'Original dictionary : {dictionary}')

# Sorting the dictionary in ascending order
sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(0))
print(f'Dictionary in ascending order : {sorted_dictionary}')

# Sorting the dictionary in descending oder
sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(0), reverse=True)
print(f'Dictionary in descending order : {sorted_dictionary}')
