"""Python program to calculate the sum of three given numbers, if the values are equal then return
thrice of their sum"""
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))
addition = first_number + second_number + third_number
print(f'The sum of {first_number}, {second_number} and {third_number} is {addition}')
if first_number == second_number == third_number:
    addition *= 3
    print(f'The thirce of {first_number + second_number + third_number} is : {addition}')
