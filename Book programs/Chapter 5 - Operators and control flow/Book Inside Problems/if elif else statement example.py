"""
2) if-elif-else statements :-
------------------------------
    It is a conditional statement used to test more than one test conditions.
    The conditions are executed from top to bottom
    If there are more than two alternatives to select, then the nested-if statements are used
"""
"""Python program to check if the number is positive or negative or neutral"""

number = int(input("Enter the number : "))
if number > 0:
    print(f'The number {number} is a positive number')
elif number == 0:
    print(f'The number {number} is a neutral number')
else:
    print(f'The number {number} is a negative number')
