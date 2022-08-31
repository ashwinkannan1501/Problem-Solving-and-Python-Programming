"""
Operators :-
-------------
    The Operators is a symbol. It is used to perform mathematical operations. Operators are the constructs which can
manipulate the value of operands.
    Example :- 'a + b = c', where 'a', 'b' are operands, 'c' is a result and '+' is a operator.

    There are 6 classifications of operators in python. They are :-
    1) Arithmetic Operators
    2) Relational (or) Comparison Operator.
    3) Boolean (or) Logical Operator.
    4) Bitwise Operator.
    5) Assignment Operator.
    6) Special Operator.

1) Arithmetic Operators :-
----------------------------
    The Arithmetic Operators is used to perform the mathematical operations like '+', '-', '*', '/', '%', '//', '**'
"""


# Python program using arithmetic operators.

def arithmetic_operators(first_number, second_number):
    # Addition (+)
    print(f'The addition of {first_number} + {second_number} is : {first_number + second_number}')
    # Subtraction (-)
    print(f'The subtraction of {first_number} - {second_number} is : {first_number - second_number}')
    # Multiplication (*)
    print(f'The multiplication of {first_number} x {second_number} is : {first_number * second_number}')
    # Division (/)
    print(f'The division of {first_number} / {second_number} is : {first_number / second_number}')
    # Modulus (%)
    print(f'The modulus of {first_number} % {second_number} is : {first_number % second_number}')
    # Exponent (**)
    print(f'The exponent of {first_number} ** {second_number} is : {first_number ** second_number}')
    # Floor division (//)
    print(f'The floor division of {first_number} // {second_number} is : {first_number // second_number}')


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

arithmetic_operators(first_number=first_number, second_number=second_number)
