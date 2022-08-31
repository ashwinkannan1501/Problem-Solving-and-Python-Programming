# python program to unzip a list of tuples into individual lists
list_tuples = [(1, 2, 3,), (4, 5, 6), (7, 8, 9)]
print(f'The unzip of the list(tuple) ({list_tuples}) is : {list(zip(*list_tuples))}')
