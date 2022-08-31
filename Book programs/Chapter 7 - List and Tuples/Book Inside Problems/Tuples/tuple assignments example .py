# tuple assignments example

# Python program to swap two numbers
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

print(f'Before swapping : first number = {first_number} ; second number = {second_number}')

(first_number, second_number) = (second_number, first_number)

print(f'After swapping : first number = {first_number} ; second number : {second_number}')

# Multiple assignments
(a, b, c) = (20, 30, 40)
print(f'Multiple assignments : a = {a} ; b = {b} ; c = {c}')
