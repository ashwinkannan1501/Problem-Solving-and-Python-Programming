"""Python scripts to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are the square of keys"""
dictionary = dict()
for number in range(1, 16):
    dictionary[number] = number * number
print(f'The dictionary is : \n{dictionary}')
