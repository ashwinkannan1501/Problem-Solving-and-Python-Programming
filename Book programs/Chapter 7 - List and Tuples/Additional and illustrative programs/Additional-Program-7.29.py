# Python program to find the repeated items of a tuple
duplicate_tuple_elements = (1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10)
print(f'Duplicate elements : {duplicate_tuple_elements}')
eight = duplicate_tuple_elements.count(8)
nine = duplicate_tuple_elements.count(9)
print(f'No:of:times the number "8" found in the tuple : {eight}')
print(f'No:of:times the number "9" found in the tuple : {nine}')
