# Python program to calculate the sum of three numbers, if the values are equal then return the thrice of their sum

x = int(input("Enter the first number : "))  # Read the first number from the user
y = int(input("Enter the second number : "))  # Read the second number from the user
z = int(input("Enter the third number : "))  # Read the third number from the user

if x == y == z:  # Check if the three numbers are equal
    total = x + y + z  # Add the three numbers
    total *= 3  # Calculate the thrice of the sum
    print(f"Thrice of sum of {x}, {y}, {z} is : {total}")  # Print the result
else:  # Check if the 3 numbers are not equal
    total = x + y + z  # Calculate the addition of three numbers
    print(f"Sum of {x}, {y}, {z} is : {total}")  # Print the result
