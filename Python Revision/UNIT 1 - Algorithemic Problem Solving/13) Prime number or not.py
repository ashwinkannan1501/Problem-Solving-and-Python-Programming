# Prime number or not

number = int(input("Enter a number : ")) # Getting a integer value from the user

if(number > 1): # Check if the number is > 1
    for index in range(2, number, 1): # Iterate using for loop
        if(number % index == 0): # Check if remainder is 0
            print(f"The number '{number}' is not a prime number") # Display the appropriate result
            break
    else:
        print(f"The number '{number}' is a prime number") # Display the appropriate result when for loop fails
else:
    print("The number '{number}' is not a prime number") # Display the appropriate result if the number is <= 1
