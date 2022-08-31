# Python divmod()
"""The divmod() function takes two numbers and returns a pair of numbers (a tuple) consistng of
their quotient and remainder
SYNTAX : divmod(x, y)
         where - x is a numerator (a non-complex number)
                 y is a denominator (a non-complex number)"""


def division_modulus(numerator, denominator):
    return f'The divmod() function of numerator ({numerator}) and denominator ({denominator}) is : ' \
           f'{divmod(numerator, denominator)}'


numerator = int(input("Enter a numerator : "))
denominator = int(input("Enter a denominator : "))
print(division_modulus(numerator, denominator))
