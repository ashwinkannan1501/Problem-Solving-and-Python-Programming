# Python Program to check whether a number is perfect or not
def perfect_number(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
            return total == number


number = int(input("Enter a number : "))
print(perfect_number(number))
