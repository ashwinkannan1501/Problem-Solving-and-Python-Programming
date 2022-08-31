# Python enumerate() function
"""The enumerate() function adds the counter to an iterable and returns it to an enumerated object
SYNTAX : enumerate(iterable, start = 0)
         where 'iterable' - a sequence, an iterator or object that supports iterations
                'start' (optional) - enumerate() function starts counting from this number. Initially 0"""
enumerated_object = input("Enter the string : ")
enumerated_object = list(enumerated_object.split(","))
print(f'Enumerated object = {list(enumerate(enumerated_object, 1))}')
print(f'Data Type : {type(enumerate(enumerated_object))}')
