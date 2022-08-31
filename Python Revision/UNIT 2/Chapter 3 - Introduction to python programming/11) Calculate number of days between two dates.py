# Python Program to calculate the number of days between two dates

import datetime  # Import the "datetime" module

first_date = datetime.date(2022, 12, 15)  # Enter the first date using "datetime.date()" function
last_date = datetime.date(2023, 12, 15)  # Enter the second date using "datetime.date()" function

difference_days = last_date - first_date  # Calculate the difference dates

print(f"{last_date} - {first_date} = {difference_days.days}")  # Print the difference in dates using "days" method
