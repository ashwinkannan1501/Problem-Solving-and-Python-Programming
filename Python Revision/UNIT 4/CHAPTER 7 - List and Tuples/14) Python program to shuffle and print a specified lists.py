# Python program to shuffle and print the specified list

from random import shuffle

lists = list(input("Enter the list values : ").split(","))
print("Original List : ", lists)

shuffle(lists)
print("Shuffled List : ", lists)
