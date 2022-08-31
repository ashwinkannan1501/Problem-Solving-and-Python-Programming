# splitlines() function
"""The splitlines() function splits teh string at line breaks and returns a list of lines in the string.
SYNTAX : string.splitlines([keepends])
where 1) keepends (optional) - If keepends is provided and its is True, line breaks are also included
        included in the list items. By default, i sets to False"""
string = "ashwin\nkannan\namutha"
print(f'String before using splitlines() function : {string}')
print(f'String after using splitlines() function : {string.splitlines()}')
