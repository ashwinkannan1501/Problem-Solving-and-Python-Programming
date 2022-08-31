# Import the 'datetime' module 
import datetime 

today_date = datetime.date.today()  # Get the today's date using 'today()' function in 'datetime.date' package

print(f"Date : {today_date.day} / {today_date.month} / {today_date.year}")  # print the date format by 'day / month / year'

current_time = datetime.datetime.now()  # Get the current time by "now()" function in "datetime.datetime" package
print(f"Time : {current_time.strftime('%H : %M : %S')}")  # print the current time by '%H : %M : %S' format
