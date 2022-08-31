# Operations of a file
# There are 3 basic operations in a file
# 1) Opening a file
# 2) Reading and writing the contents of a file
# 3) closing the file

# 1) Opening a file
"""The file has to be opened in order to access the data inside the file
SYNTAX : fileobject = open("filename.extension", ""fileaccessmode)"""

# 2) Reading and writing the contents of a file
"""2 a) Read - It is the operation where data is extracted from a file to be used for other purposes
SYNTAX : read = fileobject.read() 
3 a) Write - It is the operation where data is written into the file permanently 
             Only strings can be written
             Other data type requires format operator to write
SYNTAX : fileobject.write(string)"""

# 3) Close
"""A file when opened should be closed before the program is terminated. If not closed, no operation 
on this file is possible
SYNTAX : fileobject.close()"""

# Python program for file operations
# 1) Open a file
fileobject = open("E:\\Reshma picture collections\\Reshma pic 10.jpg", "rb")

# Reading and writing a file
print(f'The contents in the file are : {fileobject.read()}')
#fileobject.write("\nAshwin Kannan Amutha Reshma Kirthika Supriya")


# Closing the file
fileobject.close()
