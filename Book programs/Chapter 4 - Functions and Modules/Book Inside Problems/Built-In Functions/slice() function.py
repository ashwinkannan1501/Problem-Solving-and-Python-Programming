# Python slice() function
"""The slice() function is used to create a slice object representing the set of indices specified
by range (start, stop, step)
SYNTAX : slice (start, stop, step)
         where 1) start (optional) - starting integer where the slicing of the objects starts. By default,
                                  it starts from 0th index
                2) stop - integer until which the slicing takes place, The slicing stops at index stop-1
                3) step (optional) - integer value which determines the increment (or) decrement between each
                                  index for slicing, By default it increments by 1 """
variable_name = input("Enter your name : ")

# Slicing with using slice() function
print(f' The slicing of {variable_name} is : {slice(0, len(variable_name), 2)}')

# Slicing without using slice() function
print(f'The slicing of {variable_name} is : {variable_name[0: len(variable_name) : 2]}')
