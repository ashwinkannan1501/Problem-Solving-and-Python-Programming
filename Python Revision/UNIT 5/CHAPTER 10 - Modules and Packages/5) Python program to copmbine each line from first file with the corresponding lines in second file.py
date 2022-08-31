# Python program to combine each line from the first file with the corresponding line in second file

with open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/Demo text.txt") as f1, open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/text.txt") as f2:
    for line1,line2 in zip(f1, f2):
        print(line1 + line2)
