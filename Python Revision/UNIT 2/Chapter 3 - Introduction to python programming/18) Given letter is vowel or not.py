# Python program to test whether a passed letter is a vowel or not

character = input("Enter a character : ")  # Read a 'character' from the user

vowels = "aeiouAEIOU"  # Define the vowels

if character in vowels:  # Check if character is present in the vowels
    print(f"The character '{character}' is present in the vowels")  # Print the result
else:  # If character is not present in the vowels
    print(f"The character '{character}' is not present in the vowels")  # Print the result
