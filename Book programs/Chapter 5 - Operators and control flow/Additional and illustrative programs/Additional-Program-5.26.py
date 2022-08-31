# Python program to find the GCD of two numbers
first_number = int(input("Enter the first number : "))
second_number = int(input("Enter te second number : "))
for i in range(1, first_number+1):
    if (first_number % i == 0) and (second_number % i == 0):
        gcd = i
print(f'The GCD of {first_number} and {second_number} is : {gcd}')
