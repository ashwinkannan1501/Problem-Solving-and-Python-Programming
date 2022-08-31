"""Python script to generate and prints a dictionary that contains a number (between 1 to n)
in the form (x, X*X)"""
number = int(input("Enter the number : "))
dictionary = dict()
for i in range(1, number+1):
    dictionary[i] = i*i
print(f'The dictionary is : {dictionary}')