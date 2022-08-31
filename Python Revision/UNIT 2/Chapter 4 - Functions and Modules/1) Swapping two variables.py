# Python program to swap two variables

def swap(i, j):
    i, j = j, i
    return i, j


a = eval(input("Enter a value : "))
b = eval(input("Enter b value : "))

print(f"Before swapping : a = {a}, b = {b}")

result = swap(a, b)

print(f"After Swapping : a = {result[0]}, b = {result[1]}")
