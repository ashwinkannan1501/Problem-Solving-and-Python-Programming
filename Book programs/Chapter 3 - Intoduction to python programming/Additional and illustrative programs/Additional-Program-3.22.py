# Python program that add two objects if both objects are in integer type
try:
    first_object = int(input("Enter the first object : "))
    second_object = int(input("Enter the second object : "))
    print(f'The addition of {first_object} and {second_object} is : {first_object + second_object}')
except ValueError:
    print("The number should be of integer data type")
else:
    print("The program is executed successfully")
finally:
    print("The program terminates...... Good Bye :)")