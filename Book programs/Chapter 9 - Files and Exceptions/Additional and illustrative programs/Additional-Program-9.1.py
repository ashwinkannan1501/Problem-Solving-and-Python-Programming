# Python program for word count
filename = open("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\demo.txt", "r")
word = input("Enter the word : ")
count = 0
"""for line in filename:
    word = line.split()
    for i in word:
        if i == word:
            count += 1"""

while word in filename:
    count += 1

print(f'No of times does the word ({word}) occurres in the demo.txt file is : {count}')
