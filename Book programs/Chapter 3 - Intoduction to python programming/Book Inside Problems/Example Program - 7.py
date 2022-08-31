"""
Sets :-
----------
    It is a collection of unordered elements.
    It is represented as '{}'
    It eliminates/omitted the duplicate value
    It doesn't have indexes
    It is immutable (i.e) Not Changeable
    It doesn't support list and dictionary data types
"""

sets = set(input("Enter the set values : ").split(","))
print(f'The Set values are : {sets}')
print(f'The type of {sets} is : {type(sets)}')
