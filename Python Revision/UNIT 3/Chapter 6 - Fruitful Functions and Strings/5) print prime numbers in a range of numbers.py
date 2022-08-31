# Python program to print the prime numbers in a range of numbers

limit = int(input("Enter the limit : "))

for number in range(2, limit + 1):
    for index in range(2, number):
        if(number % index == 0):
            print(number, " is not a prime number")
            break
    else:
        print(number, " is a prime number")
    
