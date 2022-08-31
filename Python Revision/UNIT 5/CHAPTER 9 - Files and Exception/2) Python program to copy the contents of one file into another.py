# Python program to copy the contents of one file into another

file1 = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/Demo text.txt", 'r')
file2 = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/text.txt", 'a')

content = file1.read()
print("Contents of file 1 is : ", content)

for line in content:
    file2.write(line)

#print("Contents of file 2 is : ", file2.read())

file1.close()
file2.close()

