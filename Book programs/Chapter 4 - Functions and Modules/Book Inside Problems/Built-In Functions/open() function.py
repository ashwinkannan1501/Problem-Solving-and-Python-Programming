# Python open() function
"""The open() function opens the file (if possible) and returns a corresponding file object
SYNTAX : open(file path, filemode = 'r', buffering = -1, encoding = None, errors = None, newline = None,
        closefd = True, opener = None)
        where 1) file path - Giving file path name (representing a file system path)
              2) mode (optional) - mode while opening a file. If not provided, it sets default to 'r'
              3) buffering (optional) - used for setting buffering policy
              4) errors (optional) - string specifying how to handle encoding/decoding errors
              5) newline (optional) - how newlines mode works (None, '', '\n', 'r' and '\r\n')
              6) closefd (optional) - must be True (default) if given otherwise an exception will be raised
              7) opener (optional) - a custom opener must return an open file descriptor"""
fileobject = open(file="C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\javapadeditor.txt", mode="r", encoding='utf-8')
fileobject.read()
print(f'filename - {fileobject}')
print(f'file encoding = {fileobject.encoding}')
print(f'file buffer = {fileobject.buffer}')
print(f'file line buffering - {fileobject.line_buffering}')
print(f'file Readable - {fileobject.readable()}')
print(f'file writable - {fileobject.writable()}')
print(f'File mode = {fileobject.mode}')
print(f'File error - {fileobject.errors}')
fileobject.close()
print(f"File closed : {fileobject.closed}")
