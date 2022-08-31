# File methods

fileobject = open("C:\\Users\\ASHWINKANNAN\OneDrive\\Desktop\\notepad text editor application\\demo.txt", "r+")

# Reading from the file
print(f'The contents in the file are : {fileobject.read()}')

# Writing the contents into the file
fileobject.write("\nAshwin Kannan Amutha Reshma Kirthika Supriya")

# readable()
print(f'Whether the file is readable : {fileobject.readable()}')

# writable()
print(f'Whether the file is writable : {fileobject.writable()}')

# seekable()
print(f'Whether the file is seekable (SUPPORTS RANDOM ACCESS) : {fileobject.seekable()}')

# fileno()
print(f'The file number is : {fileobject.fileno()}')

# flush()
print(f'flush - {fileobject.flush()}')

# isatty()
print(f'Whether the file stream is interactive : {fileobject.isatty()}')

# readlines()
print(f'readlines() : {fileobject.readlines()}')

# tell()
print(f'Position of the file pointer : {fileobject.tell()}')

# seek()
print(f"Use to move the file pointer to the user's discretion : {fileobject.seek(5)}")

# rename()
import os

os.rename("demo.txt", "new_demo.txt")

# remove()
os.remove("C:\\Users\\ASHWINKANNAN\OneDrive\\Desktop\\notepad text editor application\\javapadeditor.txt")

# close()
fileobject.close()

# closed
print(f'Whether the file is closed : {fileobject.closed}')
