# Python Program to check if the input year is a leap year or not
year = int(input("Enter the year : "))
if (year%4) == 0:
    print(f"The year({year}) is a leap year")
else:
    print(f'The year({year}) is not a leap year')
