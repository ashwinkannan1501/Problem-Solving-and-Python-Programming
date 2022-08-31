# Program to accept n names, sort names in alphabetic order and print the result

names = list(input("Enter the names : ").split(","))
print(f'Printing names before sorting : {names}')
names.sort()
print(f'Printing names after sorting : {names}')
