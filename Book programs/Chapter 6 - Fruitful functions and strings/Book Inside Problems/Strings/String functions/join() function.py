# join() function
"""The join() function is used to joins the elements of the list into a single string, with each
element separated by a semi-colon (:) The delimiter doesn't need to semi-colon nora single character.
It can be any string.
SYNTAX : string.join(iterable)"""

# Python program to concatenate a string using join() function
string_1 = input("Enter the first string : ")
string_2 = input("Enter the second string : ")
print(f'The first string is : {string_1}')
print(f'The second string is : {string_2}')
print(f'The concatenation of {string_1} and {string_2} using join() function is : {string_1.join(string_2)}')
