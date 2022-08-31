# Python program to swap two numbers
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
print(f'Before Swapping : {first_number, second_number}')
(first_number, second_number) = (second_number, first_number)
print(f'After Swapping :  {first_number, second_number}')
