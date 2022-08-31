# Python reversed() function
"""The reversed() function is used to returns the reversed iterator of the given sequence
SYNTAX : reversed(seq)
         where seq - sequence that should be reversed
It supports range, tuple and list"""

name = input('Enter your name : ')
print(f'The reverse character of your name ({name}) is : {tuple(reversed(name))}')

sequence_range = range(1, 11)
print(f'The reversed of the range 1 to 10 is : {list(reversed(sequence_range))}')

