# Python program that checks whether a passed string is a palindrome or not

def palindrome(string):

    reversed_string = string[::-1]

    print("Original String : ", string)
    print("Reversed String : ", reversed_string)

    if string == reversed_string:
        return f"The string '{string}' is a palindrome"
    else:
        return f"The string '{string}' is not a palindrome"

string = input("Enter a string : ").lower()

print(palindrome(string))
