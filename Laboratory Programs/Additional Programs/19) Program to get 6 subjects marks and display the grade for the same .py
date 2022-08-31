# Program to get 6 subjects marks and display the grade for the same

# Getting the name of the candidate
name = input("Enter the candidate name : ")

# Getting the subject marks from the user
Probability_and_queueing_theory_subject = int(input("Enter the probability and queueing theory subject mark : "))
Database_Management_System_subject = int(input("Enter the Database Management System subject mark : "))
Operating_System_subject = int(input("Enter the Operating System subject mark : "))
Computer_Architecture_subject = int(input("Enter the Computer Architecture subject mark : "))
Software_Engineering_subject = int(input("Enter the Software Engineering subject mark : "))
Design_and_Analysis_of_Algorithm_subject = int(input("Enter the Design and Analysis of Algorithm subject mark : "))

# Total
total_marks = (Probability_and_queueing_theory_subject + Database_Management_System_subject +
              Operating_System_subject + Computer_Architecture_subject + Software_Engineering_subject +
              Design_and_Analysis_of_Algorithm_subject)

# Average marks
average_mark = total_marks / 6

# Displaying the grade
if average_mark >= 90:
    print(f"Mr.{name}...You got 'O' Grade")
elif (average_mark >= 80) and (average_mark <= 89):
    print(f"Mr.{name}....You got 'A+' Grade")
elif (average_mark >= 70) and (average_mark <= 79):
    print(f"Mr.{name}.....You got 'A' Grade")
elif (average_mark >= 60) and (average_mark <= 69):
    print(f"Mr.{name}....You got 'B+' Grade")
elif (average_mark >= 50) and (average_mark <= 59):
    print(f"Mr.{name}.....You got 'B' Grade")
else:
    print(f'Sorry Mr.{name}....You got fail mark now.....Better luck next time')
