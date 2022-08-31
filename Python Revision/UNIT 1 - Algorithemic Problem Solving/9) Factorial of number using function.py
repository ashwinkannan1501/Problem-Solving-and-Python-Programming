# Factorial of a number using Function

# Sub-Program
def factorial(number): # Define the "factorial" function
    factorial = 1
    for index in range(1, number + 1, 1): # Calculate the "factorial" value
        factorial = factorial * index
    print(f"The factorial of {number} is : {factorial}") # Display the value
        
# Main Program
number = int(input("Enter a factorial number : ")) # Get a number from the user

factorial(number) # Call the "factorial" function
