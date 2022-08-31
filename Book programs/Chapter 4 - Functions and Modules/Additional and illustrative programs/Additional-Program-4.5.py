# Python Program to sum all the numbers in a list
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Calculating the sum of all the numbers in the list with using built-in 'sum()' function
print(f'The sum of {list_numbers} is : {sum(list_numbers)}')

# Calculating the sum of all the numbers in the list without using built-in 'sum()' function
total = 0
for number in list_numbers:
    total += number
print(f'The sum of {list_numbers} is : {total}')
