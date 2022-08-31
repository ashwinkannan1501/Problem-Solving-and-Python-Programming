# Python program to accept a filename from the user and print the extension of that

# Get the filename with extension from the user and splits the filename and extension separately using "split() function"
filename_extension = input("Enter the filename with extension : ").split(".") 

print(f"The extension of filename '{filename_extension[0]}' is : {filename_extension[-1]}")  # Print the result
