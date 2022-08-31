# Python program to get two numbers and print the sum as big number that exceeds 100

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

addition = first_number + second_number

if(addition > 100):
    print(f"{addition} is the big number because it exceeds 100")
else:
    print(f"{addition} is the small number because it not exceeds 100")
