# Python program to find the multiplication table

number = int(input("Enter a multiplication number : "))
limit  = int(input("Enter a limit : "))

for i in range(1, limit + 1):
    print(f"{number} * {i} = {number * i}")
