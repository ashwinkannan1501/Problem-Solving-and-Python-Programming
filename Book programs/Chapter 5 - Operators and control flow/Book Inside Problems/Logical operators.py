"""
Boolean (or) Logical Operator :-
---------------------------------
    The Logical Operator are used to perform the certain logical operations on values and variables. These are some
special reserved keywords that carry out some logical computations. They are mostly used to combine two conditional
statements.

    There are 3 types of logical operators. They are :-
        1) Logical AND :- True if both the conditions are true, otherwise false
        2) Logical OR :- True if either one of the conditions is true, otherwise false
        3) Logical NOT :- True if the condition is false, otherwise false
"""


# Python program using logical operators
def logical_operators(first_number, second_number):
    # logical and operator (and)
    print(f'{first_number} and {second_number} is : {first_number and second_number}')
    # logical or operator (or)
    print(f'{first_number} or {second_number} is : {first_number or second_number}')
    # logical not operator (not)
    print(f'Negation of {first_number} is : {not first_number}')


first_number = int(input("Enter the first number : "))
second_number = int(input("eEnter the second number : "))

logical_operators(first_number=first_number, second_number=second_number)
