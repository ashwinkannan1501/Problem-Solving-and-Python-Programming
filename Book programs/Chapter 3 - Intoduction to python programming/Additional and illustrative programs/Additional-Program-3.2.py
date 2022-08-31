# Python program to display the current date and time
# Import the 'datetime' module to get the the date and time information
import datetime as dt
current_date_and_time = dt.datetime.now()
print(f'Current date and time : {current_date_and_time.strftime("%d-%m-%Y , %H:%M:%S")}')
print(f'Current date : {current_date_and_time.date().strftime("%d-%m-%Y")}')
print(f'Current time : {current_date_and_time.time().strftime("%H:%M:%S")}')
