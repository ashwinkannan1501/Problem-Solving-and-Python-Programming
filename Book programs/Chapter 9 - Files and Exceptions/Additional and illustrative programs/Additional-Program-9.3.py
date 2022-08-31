# File attributes in action
# Open a file in write and binary mode
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "rb")

# Display the file name
print(f'Filename : {filename.name}')

# Display the state of the file
print(f'File State : {filename.closed}')

# Print the mode of the file
print(f'File mode : {filename.mode}')

# Check whether the file is readable
print(f"File readable : {filename.readable()}")
