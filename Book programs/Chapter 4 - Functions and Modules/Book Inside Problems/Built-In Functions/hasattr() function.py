# Python hasattr() function
"""The hasattr() function returns true if an object has the given named attribute and false if it does not
SYNTAX : hasattr(object, name)
         where 1) object - object whose named attribute is to be checked
               2) name - name of the attribute to be searched"""


class Person:
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))


person = Person()

# Printing the age of a person with using 'getattr()' function
print(f'The age of {person.name} is : {getattr(person, "age")}')

# Printing the age of a person without using 'getattr()' function
print(f'The age of {person.name} is : {person.age}')

# Prints tio checks the person's attribute
print(f'Person has name? : {hasattr(person, "name")}')
print(f'Person has age? : {hasattr(person, "age")}')
print(f'Person has salary? : {hasattr(person, "salary")}')
