# Python program to shuffle and print a specified list
from random import shuffle
list_elements = input("Enter the string elements : ")
list_elements = list(list_elements.split(","))
shuffle(list_elements)
print(list_elements)
