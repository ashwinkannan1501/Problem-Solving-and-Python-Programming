# Python program to get two numbers and print the sum as big number that exceeds 100
try:
    first_number = float(input("Enter the first number : "))
    second_number = float(input("Enter the second number : "))
    if (first_number + second_number) > 100:
        print(f'The number {first_number + second_number} is considered as a biggest number')
    else:
        print(f"The number {first_number + second_number} is considered as a smallest number")
except ValueError:
    print("The input values should be of integer or float data type")
else:
    print("The program runs successfully without any failure :)")
finally:
    print("The programs terminates ...... Good Bye :)")
    