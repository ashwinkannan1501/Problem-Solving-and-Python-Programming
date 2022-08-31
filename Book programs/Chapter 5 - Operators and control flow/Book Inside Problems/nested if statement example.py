"""
Nested if statement / conditional statement :-
------------------------------------------------
    In a nested if construct, an if--elif--else construct inside another if--elif--else construct.
    Number of if statements can be nested inside one another but indentation is the way to figure out the level of nesting.
"""
# Python program for nested if statement

number = int(input("Enter the number : "))
if number > 0:
    if number == 0:
        print(f'The number {number} is a neutral number')
    else:
        print(f'The number {number} is a positive number')
else:
    print(f'The number {number} is a negative number')
