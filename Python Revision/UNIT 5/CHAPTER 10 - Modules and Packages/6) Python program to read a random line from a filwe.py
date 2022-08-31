# Python program to read a random line from a file
from random import choice

file = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/text.txt")

lines = file.read().splitlines()

print(choice(lines))
