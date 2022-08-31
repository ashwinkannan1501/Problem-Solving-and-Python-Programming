# Python Program to reverse a string
String_variable = input("Enter the random String : ")
reversed_string = ''
index = len(String_variable)
while index > 0:
    reversed_string += String_variable[index - 1]
    index -= 1
print(f'The reversed string of {String_variable} is : {reversed_string}')
