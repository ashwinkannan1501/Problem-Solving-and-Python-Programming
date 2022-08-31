# Program to find the biggest of three numbers

first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
third_number = float(input("Enter the third number : "))

if (first_number > second_number) and (first_number > third_number):
    print(f'The first number ({first_number}) is greater than second number ({second_number}) and '
          f'third number ({third_number})')

elif second_number > third_number:
    print(f'The second number ({second_number}) is greater than first number ({first_number}) and '
          f'third number ({third_number})')

else:
    print(f'The third number ({third_number}) is greater than first number ({first_number}) and '
          f'second number ({second_number})')
