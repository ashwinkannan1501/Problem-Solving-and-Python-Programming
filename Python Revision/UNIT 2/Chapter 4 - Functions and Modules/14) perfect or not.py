# Python program to check whether a number is perfect or not

def perfect(number):

    sum_value = 0

    for divisor in range(1, number):
        if(number % divisor == 0):
            sum_value += divisor

    if(sum_value == number):
        return f"The number '{number}' is a perfect number"
    else:
        return f"The number '{number}' is not a perfect number"

number = int(input("Enter a number : "))

print(perfect(number))

