# Python program to write a list contents to a file
list_contents = ["Ashwin", "Kannan", "Amutha", "Reshma", "Kirthika"]
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "w+")
for contents in list_contents:
    filename.write(contents)
    print(f"The contents in the list are : {contents}")
print(f'The contents in the file is : {filename.read()}')

