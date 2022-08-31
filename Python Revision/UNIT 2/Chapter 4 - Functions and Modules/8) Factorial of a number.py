# Python program to calculate the factorial of a number (non - negative integer)
try:
    def factorial(integer):
        if integer == 1:
            return integer
        else:
            return integer * factorial(integer - 1)


    number = int(input("Enter a number : "))

    print(f'The factorial of {number} is : {factorial(number)}')

except RecursionError:
    print("The Recursion cannot contain the negative number. So, Please provide a positive number")
