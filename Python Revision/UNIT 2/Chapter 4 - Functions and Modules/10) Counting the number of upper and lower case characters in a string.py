# Calculate the number of upper and lower case characters in a string

def upper_lower_count(words):
    upper = 0
    lower = 0

    for character in words:
        if 'a' <= character <= 'z':
            lower += 1
        else:
            upper += 1

    print(f"The number of lower case characters in the string '{words}' is : {lower}")
    print(f"The number of upper case characters in the string '{words}' is : {upper}")


string = input("Enter a string : ")

upper_lower_count(string)
