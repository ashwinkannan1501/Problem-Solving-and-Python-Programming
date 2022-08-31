# Python program to check whether an element exists within a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))
string = input("Enter the string : ")

if(string in  tuples):
    print(f"The item '{string}' is within the tuple")
else:
    print(f"The item '{string}' is not within the tuple")
    
