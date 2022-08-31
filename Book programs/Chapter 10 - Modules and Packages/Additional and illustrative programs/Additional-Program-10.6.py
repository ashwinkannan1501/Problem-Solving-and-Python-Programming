# Python program to read a random line from a file
# Import the 'random' module
import random
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r")
lines = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r").read().splitlines()
print(f'The random line is : {random.choice(lines)}')
