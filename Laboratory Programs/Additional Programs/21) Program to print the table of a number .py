# program to print the table of a number

number = int(input("Enter the number : "))
limit_number = int(input("Enter the limit number : "))

for i in range(1, limit_number+1):
    print(f'{number} x {i} = {number * i}')
