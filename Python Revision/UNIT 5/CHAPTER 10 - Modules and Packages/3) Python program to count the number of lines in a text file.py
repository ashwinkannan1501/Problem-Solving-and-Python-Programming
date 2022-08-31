# Python program to count the number of lines in a text file

file = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/text.txt", "r")

for (i,l) in enumerate(file):
    print("Length of file is : ", i+1)
