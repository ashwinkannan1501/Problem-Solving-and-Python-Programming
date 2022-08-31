# Python program to unzip a list of tuples into individual lists

lists = [(1,2), (3,4), (8,9)]
print("Unzipped list : ", list(zip(*lists)))
