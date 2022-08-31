# Python program to display the examination schedule

exam_date = input("Enter the exam date : ").split("/")  # Get the exam starting date in a list (separated by comma)


print(f"Exam starts from : {exam_date[0]} / {exam_date[1]} / {exam_date[2]}")  # Format this date
