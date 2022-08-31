# String operators example
"""The string operators are concatenation(+), repetition(*), slicing([]), range slicing([:]),
membership ("in" and "not in")"""

first_string = input("Enter the first string : ")
second_string = input("Enter the second string : ")

# Concatenation (+)
print(f'The concatenation (+) of {first_string} and {second_string} is : {first_string + second_string}')

# Repetition (*)
print(f'The repetition (*) of {first_string} into 3 times is : {first_string * 3}')
print(f'The repetition (*) of {second_string} into 3 times is : {second_string * 3}')

# Slicing ([])
print(f'The slicing ([]) of {first_string} is : {first_string[0]}')
print(f'The slicing of ([]) of {second_string} is : {second_string[0]}')

# Range slicing ([::])
print(f'The range slicing ([::]) of {first_string} is : {first_string[2:7:2]}')
print(f'The range slicing ([::]) of {second_string} is : {second_string[2:7:2]}')

# Membership ("in" and "not in")
print(f'The membership ("in") of {first_string} in {second_string} is : {first_string in second_string}')
print(f'The membership ("not in") of {first_string} not in {second_string} is : {first_string not in second_string}')
