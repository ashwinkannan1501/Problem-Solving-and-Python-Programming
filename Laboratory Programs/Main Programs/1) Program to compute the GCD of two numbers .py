# Computing the GCD of two numbers


def gcd(first_number, second_number, gcd):
    for i in range(1, second_number+1):
        if (first_number % i == 0) and (second_number % i == 0):
            gcd = i
    return f'The GCD of {first_number} and {second_number} is : {gcd}'


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

print(gcd(first_number=first_number, second_number=second_number, gcd=0))
