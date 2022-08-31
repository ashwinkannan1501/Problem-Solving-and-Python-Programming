# Keyword arguments
"""The python interpreter is abe to use the keyword provided to match the values with the parameter \
even though they are not arranged in order"""


def person(name, age):
    print(f'Name : {name}')
    print(f'Age : {age}')


name = input("Enter your name : ")
age = int(input("Enter your age : "))

person(age=age, name=name)
