# count() function
"""The count() function returns the number of occurrences of substring in the range [start, end].
Optional arguments start and end are interpreted as in slice notation
SYNTAX : string.count(substring, start, end)
where 1) substring - The string whose count is to be found
      2) start (optional) - starting index within the string where the search starts
      3) stop (optional) - ending index within the string where the search ends"""

string = input('Enter a string : ')
substring = input('Enter a string which is to be searched in the original string : ')
if substring in string:
    print(f'The count of {substring} in the {string} is : {string.count(substring)}')
else:
    print(f'There is no sub-string ({substring}) in the original string ({string})')
