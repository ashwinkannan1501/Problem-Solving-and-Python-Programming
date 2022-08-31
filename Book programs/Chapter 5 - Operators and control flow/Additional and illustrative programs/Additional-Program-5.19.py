# Python program to calculate the sum and average of n integer numbers. Input 0 to exit
def calculation(first_number, second_number, third_number):
    addition = first_number + second_number + third_number
    average = addition / 2
    print(f'The sum of {first_number, second_number, third_number} is : '
          f'{addition}')
    print(f'The average of {addition} is : {average}')


first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number : "))
third_number = float(input("Enter the third number : "))
calculation(first_number, second_number, third_number)
