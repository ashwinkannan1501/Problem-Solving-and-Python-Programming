# Python program to test whether a number is within 100 of 1000 or 2000

number = int(input("Enter a number : "))  # Read the integer value from the user

result = (abs(1000 - number) <= 100) or (abs(2000 - number) <= 100)  # Checking the number is within 100 of 1000 or 2000

print(f"The number '{number}' near thousand is : {result}")  # Print the result
