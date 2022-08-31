# Python program to find sum of data in a list

list_values = list(input("Enter the list values : ").split(","))

total = 0

for number in list_values:
    total = total + int(number)

print("List Values : ", list_values)
print("Sum of list values : ", total)
