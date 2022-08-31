# Python program to read and write to the same file

# Opening a file
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "w+")

# Appending the contents to the file
String = "Hello Everyone...This is K.Ashwin....\n" \
         "I am a programmer, coder and a hacker\n" \
         "Nice to meet you all"
filename.write(String)

# Reading the contents from the file
filename.read()

# Closing the file
filename.close()
