"""
Bitwise Operators :-
----------------------
    The bitwise operators are used to perform the bitwise calculations on integers. The integers are fist converted into
binary and then operations are performed on bit by bit. Then the result is returned in decimal format.

    The python bitwise operators works only on integers.
"""


# Python program using bitwise operators
def bitwise_operators(first_number, second_number):
    # Bitwise and (&)
    print(f'Bitwise and (&) of {first_number} and {second_number} is : {first_number & second_number}')

    # Bitwise or (|)
    print(f' Bitwise or (|) of {first_number} and {second_number} is : {first_number | second_number}')

    # Bitwise not (~)
    print(f'Bitwise not (~) of {first_number} is : {~ first_number}')

    # Bitwise xor (^)
    print(f'Bitwise xor (^) of {first_number} and {second_number} is : {first_number ^ second_number}')

    # Bitwise right shift (>>)
    print(f'Bitwise right shift (>>) of {first_number} and {second_number} is : {first_number >> second_number}')

    # Bitwise left shift (<<)
    print(f'Bitwise left shift (<<) of {first_number} and {second_number} is : {first_number << second_number}')


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
bitwise_operators(first_number=first_number, second_number=second_number)
