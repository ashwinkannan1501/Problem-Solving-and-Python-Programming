# Python getattr() function
"""The getattr() method returns the value of the named attribute of an object. If not found,
it returns the default value provided to the function
SYNTAX : getattr(object, name, default) . It is equivalent to "object.name"
         where  1) object - object whose named attribute's value is to be returned
                2) name - string contains the attribute's name
                3) default (optional) - value that is returned when the named attribute is not found"""


class Person:
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))


person = Person()

# Printing the age of a person with using 'getattr()' function
print(f'The age of {person.name} is : {getattr(person, "age")}')

# Printing the age of a person without using 'getattr()' function
print(f'The age of {person.name} is : {person.age}')
