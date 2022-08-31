# Python program to print two variable values (Swapping of two numbers without using temporary variable)
try:
    first_number = float(input("Enter the first number : "))
    second_number = float(input("Enter the second number : "))
    print(f"Before swapping : first number = {first_number}, second number = {second_number}")
    (first_number, second_number) = (second_number, first_number)
    print(f'After swapping : first number = {first_number}, second number = {second_number}')
except ValueError:
    print("The input number value should be of integer or float data type")
else:
    print("The program runs successfully without any failure")
finally:
    print("The program terminates....Good Bye :)")
