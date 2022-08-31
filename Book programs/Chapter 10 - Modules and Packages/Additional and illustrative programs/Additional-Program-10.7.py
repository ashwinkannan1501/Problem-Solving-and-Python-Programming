# Python program to access if a file is closed or not
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt")
print(f'File Status : {filename.closed}')
filename.close()
print(f'File Status : {filename.closed}')
