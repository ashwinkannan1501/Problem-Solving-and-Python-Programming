# Python program to reverse a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))
print("Tuple : ", tuples)

reversed_tuple = reversed(tuples)
print("Reversed Tuple : ", tuple(reversed_tuple))
