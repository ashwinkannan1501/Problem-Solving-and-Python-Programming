# Python program to slice a tuple
tuple_elements = input("Enter the tuple_elements : ")
tuple_elements = tuple(tuple_elements.split(","))
print(f"Tuple elements are : {tuple_elements}")
list_elements = list(tuple_elements)
print(f'Slicing operation in tupe : {tuple(list_elements[:2])}')
