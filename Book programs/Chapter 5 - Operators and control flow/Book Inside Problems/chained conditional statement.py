"""Python program for chained conditional statement"""

mark = int(input("Enter the mark detail : "))

if mark >= 90:
    print(f'Grade : "S"')
elif mark >= 80:
    print(f'Grade : "A+"')
elif mark >= 70:
    print(f'Grade : "A"')
elif mark >= 60:
    print(f'Grade : "B+"')
elif mark >= 50:
    print(f'Grade : "B"')
else:
    print(f'Sorry....You are failed this time!!...  :(  ...Better luck next time .....  :)')
