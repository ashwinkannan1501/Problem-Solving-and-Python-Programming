"""
Special Operators :-
---------------------
    There are 2 types of special operators. They are :-
    1) Membership Operator
    2) Identity Operator

1) Membership Operator :-
-----------------------------
    The 'in' and 'not in' are the membership operators in python.
    They are used to check whether a value or a variable is found in a sequence (String, list, tuple, set, dictionary).
    In Dictionary, we can only test for the presence of 'key', not the 'value'.
"""
# The membership operators are "in" and "not in"
# Python program using membership operators


def membership_operators(list_elements, search_element):
    # using "in" operator -  It returns True if value is found in the sequence, otherwise return False
    print(f'{search_element} in {list_elements} is : {search_element in list_elements}')

    # using "not in" operator - It returns True if value is not found in the sequence, otherwise returns False
    print(f'{search_element} not in {list_elements} is : {search_element not in list_elements}')


list_elements = input("Enter the string list elements : ")
list_elements = list(list_elements.split(","))

search_element = input("Enter the search element : ")

membership_operators(list_elements=list_elements, search_element=search_element)
