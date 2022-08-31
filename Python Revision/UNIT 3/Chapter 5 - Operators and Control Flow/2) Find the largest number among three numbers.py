# Python program to find the largest number among the three numbers

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

if(first_number > second_number and third_number):
    print(f"{first_number} is the largest number")
elif(second_number > third_number):
    print(f"{second_number} is the largest number")
else:
    print(f"{third_number} is the largest number")
