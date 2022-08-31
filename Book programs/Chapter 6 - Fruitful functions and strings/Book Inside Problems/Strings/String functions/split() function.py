# split() function
"""The split() function is used to breaks (or) splits a string at teh specified separator and returns
a list of string
SYNTAX : string.split(separator, maxsplit)
where 1) separator (optional) - This is a delimiter. The string splits at a specified separator (eg:',' '.'  etc)
            If separator is ot specified, any whitespace character will be consider as a separator
      2) maxsplit (optional) - The maxsplit defines the maximum number of splits. The default maxsplit value is -1,
            meaning, no limit on the number of splits"""

list_string = input("Enter the list of string elements : ")
print(f'Before splitting the string elements : {list_string}')
print(f'After splitting the list elements with the whitespace character : {list_string.split()}')
print(f'After splitting the list elements with the "," : {list_string.split(",")}')
print(f'After splitting the list elements with the "." : {list_string.split(".")}')
print(f'After splitting the list elements with the "," and the maxsplit value sets to 2: {list_string.split(sep=",", maxsplit=2)}')
