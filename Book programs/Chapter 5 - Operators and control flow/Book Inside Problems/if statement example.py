"""
Conditional Statement :-
--------------------------
1) if statements :-
---------------------
    The 'if' statement is a conditional statements used to check the condition or to the control the flow of execution
of commands
"""
# Python program to check the number is positive or negative or a neutral number

number = int(input("Enter the number : "))
if number > 0:
    print(f'The number {number} is a positive number')
if number < 0:
    print(f'The number {number} is a negative number')
if number == 0:
    print(f'The number {number} is a neutral number')

