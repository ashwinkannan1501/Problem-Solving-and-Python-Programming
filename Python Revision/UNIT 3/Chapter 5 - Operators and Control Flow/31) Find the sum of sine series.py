# Python program to find the sum of the sine series

import math

def sin(x, n):
    sine = 0

    for i in range(n):
        sign = (-1) ** i
        pi = 22/7
        y = x * (pi / 180)
        sine += ((y ** (2.0 * i + 1)) / math.factorial(2 * i + 1))
    return sine

x = int(input("Enter the 'x' value in degrees : "))
n = int(input("Enter the number of terms : "))

print("The sum of sine series is : ", sin(x, n))
    
