# Program to find the factorial of a number using while loop
from math import factorial
number = int(input("Enter a number : "))
print(f'Teh factorial of a number ({number}) with using "factorial()" function is : {factorial(number)}')

factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f'The factorial of a number ({number}) without using "factorial()" function is : {factorial}')
