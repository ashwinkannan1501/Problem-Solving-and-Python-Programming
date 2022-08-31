# Python eval() function
"""The eval() function evaluates the expressions passed to this function and runs the code within the program.
It evaluates the type of the data in run time
SYNTAX : eval(expression, globals=None, locals=None)
         where 'expression' - evaluates the python code
                'globals' (Optional) - a dictionary
                'locals' (Optional) - a mapping object"""

first_number = eval(input("Enter the first number : "))
print(type(first_number))
second_number = eval(input("Enter the second number : "))
addition = first_number + second_number
print(f'The addition of {first_number} and {second_number} is : {addition}')
print(eval("first_number + 10"))
