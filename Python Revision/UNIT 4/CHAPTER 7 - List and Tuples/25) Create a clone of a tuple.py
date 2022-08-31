# Python program to create a clone of a tuple

tuples = tuple(input("Enter the tuple values : ").split(","))
print("Original Tuple : ", tuples)

cloned_tuple = tuples[:]
print("Cloned Tuple : ", cloned_tuple)

