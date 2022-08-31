# Python program to find the longest word
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt")
words = filename.read().split()
maximum_length = len(max(words))
if len(words) == maximum_length:
    print(words)
