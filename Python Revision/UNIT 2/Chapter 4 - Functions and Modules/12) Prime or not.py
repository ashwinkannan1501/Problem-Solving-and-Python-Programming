# Python program that takes a number as a parameter and check the number is prime or not
def prime(integer):
    if integer == 1:
        return f"The number '{integer}' is not a prime number"
    else:
        for index in range(2, (integer // 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (integer % index) == 0:
                return f"The number '{integer}' is not a prime number"
        else:
            return f"The number '{integer}' is a prime number"


try:
    number = int(input("Enter a number : "))
except ValueError:
    print("Please enter integer values only")

print(prime(number))
