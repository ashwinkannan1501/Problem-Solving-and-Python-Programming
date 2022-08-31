"""
Relational (or) Comparison Operator :-
----------------------------------------
    It is used to compare 2 values. It either returns 'True' (or) 'False' based on the condition.
"""


# Python program using comparison (relational) operators
def comparison_operators(first_number, second_number):
    # Equal to (==)
    print(f'{first_number} is equal to  {second_number} is : {first_number == second_number}')
    # Not equal to (!=)
    print(f'{first_number} is not equal to {second_number} is : {first_number != second_number}')
    # Greater than (>)
    print(f'{first_number} is greater than {second_number} is : {first_number > second_number}')
    # Greater than or equal to (>=)
    print(f'{first_number} is greater than or equal to {second_number} is : {first_number >= second_number}')
    # Lesser than (<)
    print(f'{first_number} is lesser than {second_number} is : {first_number < second_number}')
    # Lesser than or equal to (<=)
    print(f'{first_number}is lesser than or equal to {second_number} is : {first_number <= second_number}')


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

comparison_operators(first_number=first_number, second_number=second_number)