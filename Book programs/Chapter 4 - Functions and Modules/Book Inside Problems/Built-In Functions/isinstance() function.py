# Python isinstance() function
"""The isinstance() function is used to checks if teh object (first argument) is an instance or subclass
of class info class (second argument)
SYNTAX : isinstance(object, classinfo)
         where object - object to be checked
               classinfo - class, type, tuple of classes and types"""
number = float(input('Enter a number : '))
print(f'{isinstance(number, float)}')