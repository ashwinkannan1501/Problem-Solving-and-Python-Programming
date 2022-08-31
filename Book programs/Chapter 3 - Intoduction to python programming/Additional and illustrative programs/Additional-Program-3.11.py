# Python program to calculate the number of days between two dates
# Import the 'datetime' module
from datetime import date
first_DOB = date(2001, 12, 15)
second_DOB = date(2001, 12, 22)
result_date = second_DOB - first_DOB
print(f"The difference between {first_DOB} and {second_DOB} is : {result_date}")
