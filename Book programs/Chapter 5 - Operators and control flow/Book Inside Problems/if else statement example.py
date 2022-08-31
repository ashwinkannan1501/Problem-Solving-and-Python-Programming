"""
2) if-else statements :-
--------------------------
    The if-else statement is a conditional statement and it is used to execute only one action.
If there are 2 statements to be executed alternatively, then if-else statement is used. The if-else statement is a 2 way
branching. The condition is tested and if the result of this logical test is true, then tru statement is executed.
Otherwise false statement is executed.
"""
"""Python program to check if the number is positive or negative and displays an appropriate message"""

number = int(input("Enter the number : "))
if number >= 0:
    print(f'The number {number} is a positive number')
else:
    print(f'The number {number} is a negative number')
