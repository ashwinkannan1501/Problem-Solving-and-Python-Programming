# find() function
"""The find() function is used to return the lowest index of the substring (if found), otherwise
it returns -1
SYNTAX : string.find(sub, start, end)
where 1) sub- It's the substring to be searched in the string. It returns the position (index value) of the string where
                starts
      2) start - starting index within the string where the finds starts
      3) end - ending index within the string where the finds ends"""

string = input("Enter the string : ")
substring = input("Enter the sub-string : ")
if substring in string:
    print(f'The sub-string ({substring}) finds in the string ({string}) in {string.find(substring, 0, 100)}th position')
    print(f'The string ({string}) contains the word ({substring})')
else:
    print(f'The string ({string}) does not contains the word ({substring})')
