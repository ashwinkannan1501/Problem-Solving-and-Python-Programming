# Program to find the factorial of a number using for loop
factorial = 1
factorial_number = int(input("Enter the factorial number : "))
for i in range(1, factorial_number+1):
    factorial *= i
print(f'The factorial number ({factorial_number}) is : {factorial}')
