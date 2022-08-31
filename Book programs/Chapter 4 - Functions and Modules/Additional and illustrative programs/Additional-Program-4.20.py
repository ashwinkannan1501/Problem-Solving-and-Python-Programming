# Python program to access a function inside a function


def mul(third_number, fourth_number):
    return f'The multiplication of {third_number} and {fourth_number} is : {third_number * fourth_number}'


def add(first_number, second_number):
    return f'The addition of {first_number} and {second_number} is : {first_number + second_number}'


first_number = int(input("Enter a first number : "))
second_number = int(input("Enter a second number : "))
fourth_number = int(input("Enter a fourth number : "))
print(mul(add(first_number, second_number), fourth_number))
