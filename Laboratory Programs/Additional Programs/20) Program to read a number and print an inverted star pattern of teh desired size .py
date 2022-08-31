# Program to read a number and print an inverted star pattern of teh desired size

number = int(input("Enter the number : "))

for i in range(number, 0, -1):
    print("*" * i)
