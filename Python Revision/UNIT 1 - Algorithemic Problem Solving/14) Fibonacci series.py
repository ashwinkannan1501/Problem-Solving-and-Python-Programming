# Fibonacci series

number_limit = int(input("Enter a limit : ")) # Get a integer value from the user namely "number_limit"

first_number = 0 ; second_number = 1 # Assign f = 0 and s = 1

for index in range(1, number_limit): # looping from number 1 to n
    result = first_number + second_number # Add f + s and store it in "result"
    first_number = second_number # swap f and s 
    second_number = result # Swap s and result

print(f"The fibonacci series of '{number_limit}' is : {result}") # Display the "result" value
