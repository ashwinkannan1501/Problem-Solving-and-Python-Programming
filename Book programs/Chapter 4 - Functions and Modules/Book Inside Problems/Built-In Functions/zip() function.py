# Python zip() function
"""The zip() function takes iterables (can be zero or more), makes iterator that aggregates
elements based on the iterables passed, and returns an iterator of tuples
SYNTAX : zip(*iterables)
         where iterables - can vbe built-in iterables (list, string, tuple, dictionary) or user-defined iterables"""
list_elements = ["ashwin", "kannan", "amutha"]
print(f'The zip() function of an {list_elements} is : {list(zip(list_elements))} ')
