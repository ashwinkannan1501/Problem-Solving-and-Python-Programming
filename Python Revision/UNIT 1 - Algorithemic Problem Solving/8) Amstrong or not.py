# Amstrong or not

number = int(input("Enter a number : ")) # Get a integer value from the user namely "number"

temporary_value = number # Assign the number value into the "temprary_value" variable

sum = 0 # Assign sum = 0

while(temporary_value > 0):  # Find the sum of cubes of each digit
    digit = temporary_value % 10
    sum += digit ** 3
    temporary_value //= 10

if(number == sum) : # Display the result
    print(f"The number {number} is a amstrong number")
else:
    print(f"The number {number} is not a amstrong number")
