# Python program that takes a number as a parameter and checks the number is prime or not
def prime(number):
    for i in range(2, number, 1):
        if number % i != 0:
            return f'The number {number} is a prime number'
        else:
            return f'The number {number} is not a prime number'


number = int(input("Enter a random number : "))
print(prime(number))
