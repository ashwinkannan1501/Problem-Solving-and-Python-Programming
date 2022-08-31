# Even or odd

number = int(input("Enter a number : "))  # Get a int value from the user

if number % 2 == 0:  # Check if the remainder is 0 when the number is divided by 2
    print(f"The number '{number}' is an even number")  # Print the result
else:  # If not
    print(f"The number '{number}' is an odd number")  # Print the result
