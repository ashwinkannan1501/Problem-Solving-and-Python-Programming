# Python program to find the maximum of three numbers
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

print(f'The maximum number of {first_number}, {second_number} and {third_number} with using '
      f'max() function is : {max(first_number, second_number, third_number)}')

print("Maximum number without using max() function")
if (first_number > second_number) and (first_number > third_number):
    print(f'The maximum number is : {first_number}')
elif second_number > third_number:
    print(f'The maximum number is : {second_number}')
else:
    print(f'The maximum number is : {third_number}')
