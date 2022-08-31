# Python program to print the numbers of a specified list after removing even numbers from it

lists = list(input("Enter the list values : ").split(","))
print("Original List : ", lists)

lists = [int(number) for number in lists if int(number) % 2 != 0]
print("List after removing even numbers : ", lists)
