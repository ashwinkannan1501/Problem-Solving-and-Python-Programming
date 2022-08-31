# Python program to find the exponent of a given number


def exponentiation(number, exponent_number):
    return f'The number({number}) to the exponent (or) power({exponent_number}) is : {number ** exponent_number}'


number = int(input("Enter a number : "))
exponent_number = int(input('Enter a exponent number : '))
print(exponentiation(number, exponent_number))
