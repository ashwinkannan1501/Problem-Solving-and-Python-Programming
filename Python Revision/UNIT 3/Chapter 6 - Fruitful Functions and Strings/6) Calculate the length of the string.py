# python program to calculate the length of the string

string = input("Enter a string : ")

count = 0

for character in string:
    count += 1

print(f"Length of the string '{string}' is : {count}")

