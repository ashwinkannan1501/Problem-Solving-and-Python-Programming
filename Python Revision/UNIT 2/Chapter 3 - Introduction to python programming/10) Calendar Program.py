# Python Program to print the calendar of given month and year

import calendar  # Import the calendar module

month = int(input("Enter the month (in integers): "))  # Read month value from the user
year = int(input("Enter the year : "))  # Read year value from the user

print(calendar.month(year, month))  # Print the month of a calendar by using "month(y, m)" function
