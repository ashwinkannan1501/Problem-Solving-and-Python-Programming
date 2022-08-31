# Python Program that accepts a string and calculate the number of upper and lower case letters
string = input("Enter a string : ")
upper_case_letters = 0
lower_case_letters = 0
for i in string:
    if i.isupper():
        upper_case_letters += 1
    elif i.islower():
        lower_case_letters += 1
print(f'Original String : {string}')
print(f'Total No: of: characters in the String({string}) is : {len(string)}')
print(f'No: of: Uppercase characters in the string({string}) is : {upper_case_letters}')
print(f'No: of: Lowercase characters in the string({string}) is : {lower_case_letters}')
