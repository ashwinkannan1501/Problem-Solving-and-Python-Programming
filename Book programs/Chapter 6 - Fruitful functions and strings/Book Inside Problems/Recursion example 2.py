"""Python program to display the fibonacci series upto nth term using recursive function"""


def fibonacci_sequence(number):
    if number <= 1:
        return number
    else:
        return fibonacci_sequence(number) + fibonacci_sequence(number - 1)


number = int(input("Enter a random number : "))
if_conditions = [number > 0, number > 1]
if number > 0 and number > 1:
    print(f'The fibonacci sequence is ')
    for i in range(number):
        print(fibonacci_sequence(number))
else:
    print("Please check whether your number is positive and greater than 1")
