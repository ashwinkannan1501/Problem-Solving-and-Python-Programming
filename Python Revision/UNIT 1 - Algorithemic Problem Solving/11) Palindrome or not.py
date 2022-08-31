# Palinrome or not

word = input("Enter a word : ").lower() # Getting an string value from the user

reversed_word = word[::-1] # Reverse the string 

# Print of the string value
print("word : ", word)
print("reversed word : ", reversed_word)

# Check if both the string values are equal, then it is a "palindrome"
if(word == reversed_word):
    print(f"The word '{word}' is a palindrome")
else : # If not, then  it is not a palindrome
    print(f"The word '{word}' is not a palindrome")
