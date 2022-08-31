# Python program to count the number of strings where the string length is 2 or more and the
# first land last character are same from a given list of string

string_list = list(input("Enter the string values : ").split(","))

count = 0

if(len(string_list) >= 2 and string_list[0][0] == string_list[-1][-1]):
    count += 1

print("Length of the string : ", count)
