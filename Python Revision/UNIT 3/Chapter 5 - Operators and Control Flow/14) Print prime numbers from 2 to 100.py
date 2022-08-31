# Python programs to print the prime numbers from 2 to 100

for prime in range(2, 100):
    for number in range(2, prime):
        if(prime % number == 0):
            break
    else:
        print(prime)
