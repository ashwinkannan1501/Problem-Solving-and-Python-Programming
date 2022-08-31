# Exception handling example
# try.....except

try:
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number : "))
    print(f'The addition of {first_number} and {second_number} is : {first_number + second_number}')
    print(f'The subtraction of {first_number} and {second_number} is : {first_number - second_number}')
    print(f'The multiplication of {first_number} and {second_number} is : {first_number * second_number}')
    print(f'The division of {first_number} and {second_number} is : {first_number / second_number}')

except ZeroDivisionError:
    print(f'Please enter the non-zero number in the denominator')
except ValueError:
    print(f'Please enter only the integer value')
# except KeyboardInterrupt:
#     print(f'There is some keyboardInterruptError occurs....Please try again later')
