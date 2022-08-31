"""
Assignment Operators :-
------------------------
    The Assignment Operators are used to assign the values to the variables.
"""


# Python program using assignment operators
def assignment_operators(number):
    # Assignment operator (=)
    #number = 5
    print(f'Number =  {number}')

    # Plus equal to (+=)
    number += 5  # which is equal to 'number = number + 5'
    print(f'number += 5 = {number}')

    # minus equal to (-=)
    number -= 2  # which is equal to 'number = number - 2'
    print(f'number -= 5 = {number}')

    # multiply equal to (*=)
    number *= 5  # which is equal to 'number = number * 5'
    print(f'number *= 5 =  {number}')

    # divide equal to (/=)
    number /= 5  # which is equal to 'number = number / 5'
    print(f'number /= 5 = {number}')

    # Modulus equal to (%=)
    number %= 5  # which is equal to 'number = number % 5'
    print(f'number %= 5 = {number}')

    # floor division equal to (//=)
    number //= 5  # which is equal to 'number = number // 5'
    print(f'number //= 5 = {number}')

    # exponent equal to (**=)
    number **= 5  # which is equal to 'number = number ** 5'
    print(f'number **= 5 = {number}')

    # Bitwise and equal to (&=)
    number &= 5  # which is equal to 'number = number & 5'
    print(f'number &= 5 = {number}')

    # Bitwise or equal to (|=)
    number |= 5  # which is equal to 'number = number | 5'
    print(f'number |= 5 = {number}')

    # Bitwise xor equal to (^=)
    number ^= 5  # which is equal to 'number = number ^ 5'
    print(f'number ^= 5 = {number}')

    # Bitwise right shift equal to (>>=)
    number >>= 5  # which is equal to 'number = number >> 5'
    print(f'number >>= 5 = {number}')

    # Bitwise left shift equal to (<<=)
    number <<= 5  # which is equal to 'number = number << 5'
    print(f'number <<= 5 = {number}')


number = int(input("Enter the number : "))
assignment_operators(number=number)