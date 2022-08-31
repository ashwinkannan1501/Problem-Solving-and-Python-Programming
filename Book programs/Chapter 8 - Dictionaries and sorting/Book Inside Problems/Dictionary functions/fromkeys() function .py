# fromkeys() function
"""The fromkeys() function returns a new dictionary from the given sequence of elements with the
value provided by the user
SYNTAX : dictionary.fromkeys(sequence, value)
where 1) sequence - sequence of elements to be used as keys for the new dictionary
      2) value (optional) - value is set to each element in a dictionary. If value is not provided
            it sets to None"""

keys = input("Enter the key pair in a dictionary : ").split(",")
values = input("Enter the value pair in a dictionary : ")

dictionary = dict.fromkeys(keys, values)
print(f'The dictionary is : {dictionary}')
