# Program to find the quotient, remainder and print the result

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

quotient = first_number // second_number
remainder = first_number % second_number

print(f'The quotient of {first_number} and {second_number} is : {quotient}')
print(f'The remainder of {first_number} and {second_number} is : {remainder}')
