# Factorial of a given number

number = int(input("Enter a factorial number : ")) # Getting the input from the user

factorial = 1 # Assign factorial as 1

for index in range(1, number+1, 1): # Calculate the factorial value 
    factorial *= index
    
print(f"The factorial of {number} is : {factorial}") # Display the result

