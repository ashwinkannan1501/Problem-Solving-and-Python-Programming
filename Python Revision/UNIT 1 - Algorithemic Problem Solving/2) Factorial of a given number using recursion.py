# Factorial of a given number using recursion

def factorial(number): # Defining a "factorial" function (function definition)
    if(number == 1) :
        return number
    else :
        fact = number * factorial(number - 1) # Calculating the factorial value
        return fact
    
number = int(input("Enter the factorial number : ")) # Get the input from the user

result = factorial(number) # Calling a "factorial" function

print(f"The factorial of {number} is : {result}") # Display the factorial value
