# Python program to reverse a tuple
tuple_elements = input('Enter the tuple elements : ')
tuple_elements = tuple(tuple_elements.split(","))

"""By using 'reversed()' function, we can able to reverse a values from descending to ascending
..But we have to typecast to the particular data type"""
print(tuple(reversed(tuple_elements)))
