# Output file

import calculator

first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))

print(f"{first_number} + {second_number} = {calculator.addition(first_number, second_number)}")
print(f"{first_number} - {second_number} = {calculator.subtracion(first_number, second_number)}")
print(f"{first_number} * {second_number} = {calculator.multiplication(first_number, second_number)}")
print(f"{first_number} / {second_number} = {calculator.division(first_number, second_number)}")
