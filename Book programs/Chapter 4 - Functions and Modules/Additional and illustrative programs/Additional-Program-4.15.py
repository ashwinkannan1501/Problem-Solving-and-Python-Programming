# Python program that checks whether a passed string is palindrome or not
def palindrome(string):
    left_position = 0 ; right_position = len(string)-1
    while right_position >= left_position:
        if string[left_position] == string[right_position]:
            left_position += 1
            right_position -= 1
            return f"The string '{string}' is a palindrome"
        else:
            return f"The string '{string}' is not a palindrome"


string = input('Enter a string : ')
print(palindrome(string))
