# Python program to copy the contents of one fle into another file
filename_1 = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r")
filename_2 = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\javapadeditor.txt", "r")
for line in filename_1:
    filename_2.write(line)
    print(line)
filename_1.close() ; filename_2.close()
