# Python program to count the number of lines in a text file
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r")
count = 0
for (i, l) in enumerate(filename):
    print(f'Number of lines in a text file is : {i, l}')
    break
