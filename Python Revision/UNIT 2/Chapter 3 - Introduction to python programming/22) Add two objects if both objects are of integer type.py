# Python program to add two objects if both objects are in integer type

try:  # Try the code to check if any error occurs

    first_number = int(input("Enter the first number : "))  # Get the first number from the user
    second_number = int(input("Enter the second number : "))  # Get the second number from the user

    print(
        f"{first_number} + {second_number} = {first_number + second_number}"
    )  # Add the first number and second number and print the result


except Exception:  # If an error occur in 'try' block, catch in 'except' block
    print("The numbers should be of integer data type only")  # Print the appropriate message to the user
