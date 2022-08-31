# Python program to combine two dictionary for adding values for common keys
from collections import Counter
first_dictionary = {"Ashwin": 1, "Kannan": 2, "Amutha": 3}
second_dictionary = {"Reshma": 1, "Kirthika": 2, "Supriya": 3}
result_dictionary = Counter(first_dictionary) + Counter(second_dictionary)
print(f'The addition of {first_dictionary} and {second_dictionary} is : \n{result_dictionary}')
