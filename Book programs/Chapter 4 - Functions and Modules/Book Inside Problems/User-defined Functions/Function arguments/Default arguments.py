# Default arguments
"""It assumes a default value if a value is not provided in the function call for that argument"""


def person(name="raja", age=25):
    print(f'Name : {name}')
    print(f'Age : {age}')


person(name="ashwinkannan", age=20)
