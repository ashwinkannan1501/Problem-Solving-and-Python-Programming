# Python program to read and write to the same file

try:
    file_object = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/Demo text.txt", 'r+')
    print("Old Content : ", file_object.read())

except FileNotFoundError:
    print("The file is not found")

else:
    file_object.write("\nThis content will be replaced by me :)")
    print("New Content : ", file_object.read())

finally:
    file_object.close()
