"""Python program to accept a filename from the user and print the extension of that"""
filename = input("Enter the filename with the extension : ")
filename_extension = filename.split(".")
print(f"The extesion of the filename({filename}) is : '.{(filename_extension[-1])}' file")
