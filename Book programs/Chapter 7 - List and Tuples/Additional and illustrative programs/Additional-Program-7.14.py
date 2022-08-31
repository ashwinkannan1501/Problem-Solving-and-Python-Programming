# Python program to print the numbers of a specified list after removing even numbers from it
list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Print the numbers of a specified list after removing even numbers are : ")
for i in list_elements:
    if i % 2 != 0:
        print(i)
