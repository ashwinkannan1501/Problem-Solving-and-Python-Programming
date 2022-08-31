# Python program to check if the input is a leap year or not

def leap_year(year):
    if year % 4 == 0 or (year % 100 and year % 400) == 0:
        return f"The year '{year}' is a leap year"
    else:
        return f"The year '{year}' is not a leap year"


year = int(input("Enter the year : "))

print(leap_year(year))
