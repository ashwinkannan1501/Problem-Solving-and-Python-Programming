# Python program to print prime numbers in a range of number
for number in range(1, 21):
    for prime_number in range(2, number):
        if (number % prime_number) != 0:
            print(f'The number {number} is a prime number')
            break
        else:
            print(f'The number {number} is not a prime number')
            break
