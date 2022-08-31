"""Python program which accepts the sequence of comma-separated numbers from user and generate a list and a tuple with
those numbers """
values = eval(input("Enter the values : "))
list_elements = list(values)
tuple_elements = tuple(values)
print(f'List : {list_elements}')
print(f'Tuple : {tuple_elements}')
