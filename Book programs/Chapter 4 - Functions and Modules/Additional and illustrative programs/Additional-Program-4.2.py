# Python program to circulate the values of n variables
list_numbers = input("Enter the random integer numbers : ")
list_numbers = list(list_numbers.split(","))
for numbers in range(len(list_numbers)):
    print(list_numbers[numbers:] + list_numbers[:numbers])
