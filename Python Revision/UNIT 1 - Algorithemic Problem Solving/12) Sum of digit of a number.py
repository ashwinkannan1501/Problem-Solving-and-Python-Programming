# Sum of digit of a number

number = int(input("Enter a number : ")) # Get a integer value from the user

temp = number # Assign temp=number
add = 0 # Assign add = 0

# Calculate the sum of digit of a number
while(number > 0):
    digit = number % 10
    add = add + digit
    number = number // 10

print(f"The sum of digit of number '{temp}' is : {add}") # Display the result
