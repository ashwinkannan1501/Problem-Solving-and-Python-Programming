# Python program to write a list of content to a file

list_values = list(input("Enter the list values : ").split(","))

file = open("C:/Users/ASHWINKANNAN/OneDrive/Desktop/text.txt", "w")

for items in list_values:
    file.write(items)

file.close()

