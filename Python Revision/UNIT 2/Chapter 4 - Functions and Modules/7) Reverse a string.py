# Python program to reverse a string

def reverse(word):
    return word[::-1]

    
string = input("Enter a string : ")

print(f"The reverse of {string} is : {reverse(string)}")
