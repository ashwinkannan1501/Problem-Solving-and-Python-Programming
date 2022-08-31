# Python program to check prime numbers

number = int(input("Enter a number : "))

for x in range(2, number):
    if(number % x != 0):
        print(f"{number} is a prime number")
        break
    else:
        print(f"{number} is not a prime number")
        break
    
