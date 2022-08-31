# index() function
"""The index() function returns the index of a sub-string inside the string, otherwise it raises a
ValueError exception
SYNTAX : string.index(sub, start, end)
where 1) sub- It's the substring to be searched in the string. It returns the position (index value) of the string where
                starts
      2) start - starting index within the string where the indexing position starts
      3) end - ending index within the string where the indexing position ends"""

string = input("Enter a string : ")
substring = input(f'Enter a sub-string that contain the string ({string}) : ')
if substring in string:
    print(f'The sub-string ({substring}) finds in the string ({string}) in {string.index(substring, 0, 100)}th position')
    print(f'The string ({string}) contains the word ({substring})')
else:
    print(f'The string ({string}) does not contains the word ({substring})')
