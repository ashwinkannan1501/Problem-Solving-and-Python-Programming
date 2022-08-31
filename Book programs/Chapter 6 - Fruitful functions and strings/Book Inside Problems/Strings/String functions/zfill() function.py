# zfill() function ((or) zerofill() function)
"""The zfill() function returns a copy of the string with '0' characters padded to the left
SYNTAX : string.zfill(width)
where 1) width - The width specifies the length of the returned string from zfill() with '0' digits
        filled to the left hand side"""
string = input("Enter a string : ")
print(f'Before using zfill() function : {string}')
print(f'After using zfill() function : {string.zfill(30)}')
