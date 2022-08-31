# Python program to multiply all the items in a list

lists = list(input("Enter the list values : ").split(","))

multiply = 1

for number in lists:
    multiply *= int(number)

print("List values : ", lists)
print("The multiplication of list values is : ", multiply)
