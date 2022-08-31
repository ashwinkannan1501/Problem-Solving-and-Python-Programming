# String Palindrome

string = input("Enter the string : ")
reversed_string = string[::-1]

if reversed_string == string:
    print(f'The string ({string}) is a palindrome')
else:
    print(f'The string ({string}) is not a palindrome')
