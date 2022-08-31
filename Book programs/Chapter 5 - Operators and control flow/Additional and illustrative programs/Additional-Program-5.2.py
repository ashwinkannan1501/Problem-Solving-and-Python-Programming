# Python program to find the largest number among three numbers
try:
    first_number = float(input("Enter the first number : "))
    second_number = float(input("Enter the second number : "))
    third_number = float(input("Enter the third number : "))

    # Finding maximum number with using built-in 'max()' function
    print(f'The maximum number between {first_number}, {second_number} and {third_number} is : '
          f'{max(first_number, second_number, third_number)}')

    # Finding maximum number without using 'max()' function
    if first_number == second_number == third_number:
        print(f"All the values are equal ({first_number, second_number, third_number})")
    elif (first_number > second_number) and (first_number > third_number):
        print(f'The maximum number between {first_number}, {second_number} and {third_number} is : '
              f'{first_number}')
    elif second_number > third_number:
        print(f'The maximum number between {first_number}, {second_number} and {third_number} is : '
              f'{second_number}')
    else:
        print(f'The maximum number between {first_number}, {second_number} and {third_number} is : '
              f'{third_number}')
except ValueError:
    print("The input number should be of integer or float data type")
else:
    print("The program runs successfully without any failure :)")
finally:
    print("The program terminates ....... Good Bye :)")
