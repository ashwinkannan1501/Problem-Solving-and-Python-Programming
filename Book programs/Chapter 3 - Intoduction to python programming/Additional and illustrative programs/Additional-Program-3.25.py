"""Python Program to compute the future value of a specified principal amount,
interest rate and a number of years"""
# Import the 'math' module to do the mathematical calculations
from math import pow
principal_amount = float(input("Enter the principal amount : "))
interest_rate = float(input("Enter the interest rate : "))
no_of_years = float(input("Enter the number of years : "))
future_value = principal_amount*(pow((1+(0.01*interest_rate)), no_of_years))
print(f'Future Value : {round(future_value, 2)}')
