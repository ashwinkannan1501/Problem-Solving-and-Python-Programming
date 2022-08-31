# Python program to access a function inside a function (nested function)

def square(number):
    return f"The square of {number} is : {number ** 2}"

number = int(input("Enter a number : "))

print(square(number))
