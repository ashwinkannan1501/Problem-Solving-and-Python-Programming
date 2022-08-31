# Python program to check if the number provided by the user is an amstrong or not

number = int(input("Enter a number : "))

sum = 0

temp = number

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if(number == sum):
    print(f"{number} is an amstrong number")
else:
    print(f"{number} is not an amstrong number")
