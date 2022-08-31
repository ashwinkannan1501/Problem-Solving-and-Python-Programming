# Program to find the sum of 'N' natural numbers

number = int(input("Enter the number : "))
add = 0
count = 0
while number >= count:
    add += count
    count += 1
print(f'The sum of {number} natural number is : {add}')

