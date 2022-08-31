# Python program to combine each line from the first file with the corresponding line n the second file
filename_1 = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r")
filename_2 = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\javapadeditor.txt", "r")
for (line1, line2) in zip(filename_1, filename_2):
    print(file=line1+line2)
