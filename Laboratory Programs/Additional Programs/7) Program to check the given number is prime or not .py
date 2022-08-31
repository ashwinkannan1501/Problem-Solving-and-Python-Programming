# Program to check the given number is prime or not

number = int(input("Enter the number : "))
if number > 1:
    for i in range(2, number):
        if (number % i) != 0:
            print(f'The number ({number}) is a prime number')
            break
        else:
            print(f'The number ({number}) is not a prime number')
            break
else:
    print(f'The number should be greater than 1')

