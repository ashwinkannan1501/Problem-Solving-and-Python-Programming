"""Recursion - It is a process of calling a function again and again by itself until some condition
is satisfied """
# Example program -1
# Python program to find the factorial of a given number by using recursion


def factorial(number):
    if number == 1 or number == 2:
        return number
    else:

        return number * factorial(number-1)


number = int(input("Enter a random number : "))
factorial_result = factorial(number=number)
print(f'The factorial of a number {number} is : {factorial_result}')
