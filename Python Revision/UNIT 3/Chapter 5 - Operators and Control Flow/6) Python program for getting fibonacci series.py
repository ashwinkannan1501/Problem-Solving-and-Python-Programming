# Python program for getting fibonacci series

limit = int(input("Enter a limit : "))

a = 0
b = 1

while(a < limit):
    print(a)
    a, b = b, a + b
    
