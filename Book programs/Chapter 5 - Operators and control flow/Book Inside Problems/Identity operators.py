"""
Identity Operator :-
----------------------
    The 'is' and 'is not' are the identity operators.
    They are used to check if two values are identical or not (refers to same object or not).
"""

# Identity operators are "is" and "is not"
# python program using identity operators


def identity_operators(string, search_string):
    # using "is" operator - It Returns True if the operands are identical (refers to the same object), otherwise returns False.
    print(f'{string} is {search_string} : {string is search_string}')
    #print(string is string)

    # using "is not" operator - It returns True if the operands are not identical (doesn't refer to the same object), otherwise returns False.
    print(f'{string} is not {search_string}: {string is not search_string}')


string = int(input('Enter the integer number : '))
search_string = int(input('Enter the integer number to be searched : '))

identity_operators(string=string, search_string=search_string)
