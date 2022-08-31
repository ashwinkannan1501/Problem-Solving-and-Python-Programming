# Python program for integer arithmetic
try:
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number : "))
    print(f'The addition of {first_number} and {second_number} is : {first_number + second_number}')
    print(f'The subtraction of {first_number} and {second_number} is : {first_number - second_number}')
    print(f'The multiplication of {first_number} and {second_number} is : {first_number * second_number}')
    print(f'The division of {first_number} and {second_number} is : {first_number / second_number}')
    print(f'The exponentiation  of {first_number} and {second_number} is : {first_number ** second_number}')
    print(f'The floor division of {first_number} and {second_number} is : {first_number // second_number}')
    print(f'The modulus of {first_number} and {second_number} is : {first_number % second_number}')
except ValueError:
    print("The input number value should be of integer data type")
else:
    print("The program runs successfully without any failure")
finally:
    print("The program terminates....Good Bye :)")
