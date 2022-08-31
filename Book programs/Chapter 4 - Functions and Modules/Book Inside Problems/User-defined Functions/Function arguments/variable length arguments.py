# Variable length arguments
"""I we want to specify more than specified arguments while defining the function, variable length
arguments are used. It is denoted by (*) symbol before parameter"""


def person(name, *age):
    print(f'Name : {name}')
    print(f'Age : {age}')


person("Ashwinkannan", 20, 30, 40)
