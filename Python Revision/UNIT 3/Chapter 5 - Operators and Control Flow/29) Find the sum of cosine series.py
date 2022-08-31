# Python program to find the sum of cosine series

import math

def cosine(x, n):
    cosx = 1
    sign = -1

    for i in range(2, n, 2):
        pi = 22/7
        y = x * (pi / 180)
        cosx = cosx + (sign * (y ** i))/ math.factorial(i)
        sign = -sign
    return cosx

x = int(input("Enter the 'x' value in degrees : "))
n = int(input("Enter the number of terms : "))
print("The sum of cosine series : ", cosine(x, n))
