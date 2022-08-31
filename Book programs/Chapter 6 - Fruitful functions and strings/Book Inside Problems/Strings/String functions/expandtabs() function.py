# expandtabs() function
"""The expandtabs() function returns a string copy with all tab characters '\t' replaced with the
whitespace characters until the next multiple of tabsize parameter. The expandtabs() function takes
an integer tabsize arguments. The default tabsize is 8.
SYNTAX : string.expandtabs(tabsize)
where tabsize - size of an tab-space or whitespace characters"""

# Program to replace all tab characters '\t' with whitespace characters in a string
string = "ashwin\tkannan\tamutha"
print(f'Before using expandtabs() function : {string}')
print(f'After using expandtabs() function : {string.expandtabs(tabsize=10)}')
