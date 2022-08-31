# Python program to sum all the items in a list

lists = list(input("Enter the list value : ").split(","))

total = 0

for number in lists:
    total += int(number)

print("List values : ", lists)
print('The sum of list values is : ', total)
