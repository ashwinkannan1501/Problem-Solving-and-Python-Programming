# Required arguments
""" 1) Required arguments are the arguments passed to a function in a correct positional order
    2) The number of arguments in a function call should match exactly with the function definition"""


def person(name, age):  # parameters, function definition
    print(f'Name : {name}')
    print(f'Age : {age}')


person(name="Ashwinkannan", age=20)  # arguments , function calling
