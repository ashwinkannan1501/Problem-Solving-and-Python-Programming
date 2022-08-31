# Program to find the first N terms prime numbers

number = int(input("Enter the number : "))
count = 1
num = 2

while count < number:
    for i in range(2, num):
        if num % i == 0:
            break

    else:
        print(num)
        count += 1
    num += 1
