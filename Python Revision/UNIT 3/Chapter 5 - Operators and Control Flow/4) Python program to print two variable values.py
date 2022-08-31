# Python program to print two variable values

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

print(f"Before Swapping : first number = {first_number}, second number = {second_number}")

first_number, second_number = second_number, first_number
print(f"After Swapping : first number = {first_number}, second number = {second_number}")
