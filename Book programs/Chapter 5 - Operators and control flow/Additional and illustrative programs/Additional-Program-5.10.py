# Python program to check if the number provided by the user is an armstrong number or not
number = int(input("Enter a random number : "))
temporary_variable = number
s = 0
while number != 0:
    d = number % 10
    s = s + d ** 3
    number //= 10
if temporary_variable == s:
    print(f'The number {temporary_variable} is an armstrong number')
else:
    print(f'The number {temporary_variable} is not an armstrong number')

