# Python program to add natural numbers up to 10
natural_number = int(input("Enter the maximum natural number : "))
add = 0
initialize = 1
while initialize <= natural_number:
    add += initialize
    initialize += 1
print(f'The sum of natural number is : {add}')
