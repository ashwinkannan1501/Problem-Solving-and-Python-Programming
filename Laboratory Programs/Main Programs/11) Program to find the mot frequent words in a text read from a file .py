# Python program to find the most frequent words in a text from a file
from collections import Counter
fileobject = open(file="C:/Users/ASHWINKANNAN/OneDrive/Desktop/notepad text editor application/demo.txt", mode="r")
print(f'Number of words in a file is : {fileobject.read().split()}')
