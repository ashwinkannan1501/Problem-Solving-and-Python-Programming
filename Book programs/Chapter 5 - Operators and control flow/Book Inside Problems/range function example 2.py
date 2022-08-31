# Python program to check if the number is prime or not
number = int(input("Enter a random number : "))
for prime in range(2, number):
    if (number % prime) != 0:
        print(f'The number {number} is a prime number')
        break
    if (number % prime) == 0:
        print(f'The number {number} is not a prime number')
        break
