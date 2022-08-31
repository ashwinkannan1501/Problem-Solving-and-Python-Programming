# Python __import__() function
"""The __import__() function is an advanced function that is called by the import statement
SYNTAX : __import__(name, globals=None, locals=None, fromlist=(), level=0)
         where 1) name - name of the module to be imported
               2) globals and locals - determines how to interpret name
               3) fromlist - objects or sub-modules that should be imported by name
               4) level - specifies whether to use absolute or relative imports"""
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))