# Python program to check whether a file exists

import os  # Import the "os" module

file = open("abc.txt")  # Open the file using 'open()' function in 'r' read mode

if os.path.isfile("abc.txt"):  # Check if the file is in the path
    print("File exists")  # Print the appropriate message

else:  # If the file is not in the path
    print("File doesn't exists")  # Print the appropriate message
