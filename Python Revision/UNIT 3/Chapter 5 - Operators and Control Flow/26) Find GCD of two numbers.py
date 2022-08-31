# Python program to find the GCD of two numbers

from math import gcd

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

# With using 'gcd()' function
print("With using 'gcd()' function : ")
print(f"The GCD of {first_number} and {second_number} is : {gcd(first_number, second_number)}")

# Without using 'gcd()' function
for number in range(1, first_number + 1):
    if(first_number % number == 0 and second_number % number == 0):
        gcd = number
print("Without Using 'gcd()' function")
print(f"The GCD of {first_number} and {second_number} is : {gcd}")
