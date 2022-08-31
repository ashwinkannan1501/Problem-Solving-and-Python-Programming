# Python Program that accepts an integer (n) and computes the value of n + nn + nnn

n = int(input("Enter the n value : ")) # Get the n value from the user

nn = n ** 2  # Multiply n 2 times

nnn = n ** 3  # Multiply n 3 times

print(f'The Value of n + nn + nnn is : {n + nn + nnn}')  # Print the sum of "n + nn + nnn"
