# replace() function
"""The relace() function will find and replace the old string with a new string. If the old string
is not found, it returns the copy of the original string
SYNTAX : string.replace(old, new , count)
where 1) old - old substring to replace
      2) new - replace new substring with the new substring
      3) count (optional) - the number of times to replace the old substring with new substring"""

string = input("Enter a string : ")
old_substring = input("Enter a old substring : ")
new_substring = input(f"Enter a new substring to replace the old substring ({old_substring}) : ")
print(f'Before replace() function : {string}')
print(f'After replace() function : {string.replace(old_substring, new_substring, 3)}')
